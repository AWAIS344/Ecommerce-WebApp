
from app.models import Products,ProductImage , Size ,Color , CartItem
from django.db.models import Prefetch
from django.shortcuts import render , redirect , get_object_or_404 , HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View

from django.http import JsonResponse
from django.contrib import messages  # For user feedback

from django.db.models import Avg

from django.contrib.auth import login 
from app.forms import SubscribeForm , User_Reg , PriceFilterForm , ReviewForm, MessageForm 

# Create your views here.

def Homepage(request):
    products = Products.objects.all()
    new_arrivals=Products.objects.all().order_by("-last_update")[0:8]

    
    sub_form=SubscribeForm()
    success = None
    success_msg=""
    if request.method=='POST':
        sub_form=SubscribeForm(request.POST)
        if sub_form.is_valid():
            sub=sub_form.save()
            request.session['subscribed']=True
            success=True
            success_msg='You have been Subscribed'

            return HttpResponseRedirect(reverse(Homepage))
    
    context = {"product": products,"new_arrivals":new_arrivals,"sub_form":sub_form,"success":success,"success_msg":success_msg}
    return render(request, "app/home.html", context ,)

def shoppage(request):
    # Get all products
    products = Products.objects.all()

    print(products)



    # Get all sizes for the size filter
    all_sizes = Size.objects.all().order_by('name')

    all_colors=Color.objects.all()

    selected_colors=request.GET.getlist('color')
    # Get selected sizes from the GET request
    selected_sizes = request.GET.getlist('size')
    # Apply size filtering if selected sizes are available
    if selected_sizes:
        products = products.filter(sizes__name__in=selected_sizes).distinct()

    if selected_colors:
        products = products.filter(color__name__in=selected_colors).distinct()
    else:
        selected_colors = []

    
    # Price filter form
    price_form = PriceFilterForm(request.GET)
    if price_form.is_valid():
        min_price = price_form.cleaned_data.get('min_price')
        max_price = price_form.cleaned_data.get('max_price')
        
        if min_price is not None:
            products = products.filter(price__gte=min_price)
        if max_price is not None:
            products = products.filter(price__lte=max_price)
    

    # Annotate products with average rating
    products = products.annotate(avg_rating=Avg('reviews__rating')).order_by("-last_update")[:16]

    # Round average ratings to nearest integer
    for product in products:
        product.average_rating = int(round(product.avg_rating)) if product.avg_rating else 0

    # Pass context data to template
    context = {
        "products": products,
        "stars_range": range(1, 6),  # To loop for 1-5 stars in the template
        "all_sizes": all_sizes,
        "selected_sizes": selected_sizes,
        "price_filter_form": price_form,  # Include the price filter form in context
        "all_colors":all_colors,
        "selected_colors":selected_colors,
        }
    
    return render(request, "app/shop.html", context)

def Product(request,slug):
    product = get_object_or_404(Products, slug=slug)
    form=ReviewForm()
    msgForm=MessageForm()

    if request.POST:
        form_type=request.POST.get("form_type")
        if form_type=="Submit Review":
            form=ReviewForm(request.POST)
            if form.is_valid():
                review=form.save(commit=False)
                review.product=product
                review.user=request.user
                print("hello g")
                review.save()
                return HttpResponseRedirect(reverse("product",kwargs={'slug':slug}))
        elif form_type=="Send Message":
            print("Hello ")
            msgForm=MessageForm(request.POST)
            print("request success Post")
            if msgForm.is_valid():
                print("Form Validaeted")
                msg=msgForm.save(commit=False)
                print("Commit Pass")
                msg.user=request.user
                print("User Pass")
                msg.product=product
                print("Prodct Pass")
                msg.save()
                print("Saved")
                return HttpResponseRedirect(reverse("product",kwargs={'slug':slug}))
            else:
                print("below")
                print("Form errors:", msgForm.errors)

        

    sizes=product.sizes.all()
    colors=product.color.all()

# Calculate average rating for the product
    avg_rating = product.reviews.aggregate(avg_rating=Avg('rating'))['avg_rating']
    avg_rating = int(round(avg_rating)) if avg_rating else 0  # Round to the nearest integer
    
    # Create a range of 1 to 5 for star rendering
    percentage=0
    saving=0
    stars_range = range(1, 6)
    if product.striked_price:
        saving=(product.striked_price)-(product.price)
        percentage=100-((round(product.price/product.striked_price,2)*100))

    

    avg_rating = product.reviews.aggregate(avg_rating=Avg('rating'))['avg_rating']  # Aggregate instead of annotate

 

    context={"products":product,"percentage":percentage,"saving":saving,"sizes":sizes,"stars_range": range(1, 6),'average_rating': avg_rating,  # Rounded average rating
        'stars_range': stars_range,"form":form,"msgForm":msgForm,"colors":colors}
    return render(request,"app/product.html",context)

def CartView(request):
    if request.method == "POST":
        # Handle form submission
        note = request.POST.get("note", "")
        terms = request.POST.get("terms", None)

        if not terms:
            # Add an error message and reload the cart page
            messages.error(request, "You must agree to the terms and conditions.")
            return redirect("cart")  # Replace 'cart' with your URL name for CartView

        # Save the note and terms in the session (or pass it directly)
        request.session["note"] = note

        # Redirect to the checkout page
        return redirect("checkout")  # Replace 'checkout' with your URL name for the checkout view

    # Normal GET request to display the cart
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = 0

    for item in cart_items:
        item.subtotal = item.product.price * item.quantity
        total_price += item.subtotal

    context = {
        "cart_items": cart_items,
        "total_price": total_price,
    }
    return render(request, "app/cart.html", context)

def update_cart_item(request):
    if request.method == "POST":
        item_id = request.POST.get("item_id")
        new_quantity = int(request.POST.get("quantity"))

        try:
            # Fetch the cart item and update quantity
            cart_item = CartItem.objects.get(id=item_id, user=request.user)
            cart_item.quantity = new_quantity
            cart_item.save()

            # Calculate new subtotal and total price
            subtotal = cart_item.product.price * cart_item.quantity
            cart_items = CartItem.objects.filter(user=request.user)
            total_price = sum(item.product.price * item.quantity for item in cart_items)

            return JsonResponse({
                "message": "Cart updated successfully",
                "subtotal": subtotal,
                "total_price": total_price,
            })
        except CartItem.DoesNotExist:
            return JsonResponse({"error": "Cart item not found"}, status=404)
    return JsonResponse({"error": "Invalid request"}, status=400)

# def AddToCart(request):
#     if request.method == "POST":
#         product_slug = request.POST.get("slug")
#         quantity = int(request.POST.get("quantity", 1))
#         color = request.POST.get("color")
#         size = request.POST.get("size")

#         # Validate color and size
#         if not color or not size:
#             return JsonResponse({"error": "Color and size are required."}, status=400)
        
#         product = get_object_or_404(Products, slug=product_slug)

#         # Check if a CartItem with the same product, color, and size already exists
#         cart_item, created = CartItem.objects.get_or_create(
#             user=request.user,
#             product=product,
#             color=color,
#             size=size,
#         )
        
#         # If the item was newly created, set the quantity
#         if created:
#             cart_item.quantity = quantity
#         else:
#             # If the item already exists, update the quantity
#             cart_item.quantity += quantity
        
#         cart_item.save()  # Save the updated cart item

#         return JsonResponse({"message": "Product added to cart", "quantity": cart_item.quantity})
    
#     return JsonResponse({"error": "Invalid request"}, status=400)


def AddToCart(request):
    if request.method == "POST":
        product_slug = request.POST.get("slug")
        quantity = int(request.POST.get("quantity", 1))  # Get the quantity sent from frontend
        color = request.POST.get("color")
        size = request.POST.get("size")

        # Debugging line: Print the received quantity
        print(f"Received quantity in backend: {quantity}")  # Debugging line
        
        if not color or not size:
            return JsonResponse({"error": "Color and size are required."}, status=400)
        
        product = get_object_or_404(Products, slug=product_slug)

        # Check if a CartItem with the same product, color, and size already exists
        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,
            product=product,
            color=color,
            size=size,
        )
        
        if created:
            # If the item is new, set the quantity to the specified value
            cart_item.quantity = quantity
        else:
            # If the item already exists, update the quantity
            cart_item.quantity += quantity  # Adding the new quantity to the existing one
        
        cart_item.save()  # Save the updated cart item

        return JsonResponse({"message": "Product added to cart", "quantity": cart_item.quantity})
    
    return JsonResponse({"error": "Invalid request"}, status=400)




def AboutUs(request):
    context={}
    return render(request,"app/aboutus.html",context)

def Not_found_Error(request):
    context={}
    return render(request,"app/404.html",context)

def Comming_Soon(request):
    context={}
    return render(request,"app/comming_soon.html",context)

def Blog(request):
    context={}
    return render(request,"app/blog.html",context)

# def Login(request):
#     context={}
#     return render(request,"registration/login.html",context)

# def Register(request):
#     form=User_Reg()
#     if request.POST:
#         form=User_Reg(request.POST)
#         if form.is_valid():
#             print("hi")
#             user=form.save()
#             login(request,user)
#             return redirect("/")
#     context={"form":form}
#     return render(request,'registration/create_account.html',context)

def Register(request):
    print("View triggered")  # Debug: Check if the view is accessed
    form = User_Reg()
    if request.method == 'POST':
        print("POST request received")  # Debug: Check POST request
        form = User_Reg(request.POST)
        if form.is_valid():
            print("Form is valid")  # Debug: Check form validation
            user = form.save()
            login(request, user)
            print(f"User {user.username} created and logged in")  # Debug: Check user creation
            return redirect("/")
        else:
            print("Form errors:", form.errors)  # Debug: Output form errors
    context = {"form": form}
    return render(request, 'registration/create_account.html', context)


def Wishlist(request):
    context={}
    return render(request,"app/wishlist.html",context)

def Contactus(request):
    context={}
    return render(request,"app/contact.html",context)