 
from app.models import Products,ProductImage , Size ,Color , CartItem , Order , OrderItem,Brand,Tag,FAQs
from django.db.models import Prefetch
from django.shortcuts import render , redirect , get_object_or_404 , HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View

from django.http import JsonResponse
from django.contrib import messages  # For user feedback

from django.db.models import Avg

from django.contrib.auth import login 
from app.forms import SubscribeForm , User_Reg , PriceFilterForm , ReviewForm, MessageForm,CheckoutForm , PaymentForm

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
    all_tags=Tag.objects.all()

    percentage=0


    for i in products:
        if i.striked_price:
            percentage=100-((round(i.price/i.striked_price,2)*100))
            

    top_product=Products.objects.all().order_by("-view_count")[0:4]

    all_brands = Brand.objects.all()
    selected_tags = request.GET.getlist('tag')


    if selected_tags:
        products = products.filter(tag__slug__in=selected_tags).distinct()

    selected_brands = request.GET.getlist('brand')

    if selected_brands:
        products = products.filter(brand__in=selected_brands)

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
        "percentage":percentage,
        "top_product":top_product,
        "all_brands":all_brands,        
        "products": products,
        "stars_range": range(1, 6),  # To loop for 1-5 stars in the template
        "all_sizes": all_sizes,
        "selected_sizes": selected_sizes,
        "price_filter_form": price_form,  # Include the price filter form in context
        "all_colors":all_colors,
        "selected_colors":selected_colors,
        'selected_brands': selected_brands,
        "all_tags":all_tags,
        }
    
    return render(request, "app/shop.html", context)



def Product(request,slug):

    product = get_object_or_404(Products, slug=slug)
    variants = product.variants.select_related('color', 'size')
    form=ReviewForm()
    msgForm=MessageForm()

    if product.view_count is None:
        product.view_count=1

    else:
        product.view_count+=1
    
    product.save()

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

    
    print(saving)
    
    print(percentage)
    

    avg_rating = product.reviews.aggregate(avg_rating=Avg('rating'))['avg_rating']  # Aggregate instead of annotate

 

    context={"products":product,"percentage":percentage,"saving":saving,"sizes":sizes,"stars_range": range(1, 6),'average_rating': avg_rating,  # Rounded average rating
        'stars_range': stars_range,"form":form,"msgForm":msgForm,"colors":colors,"variants":variants,"labels":labels}
    return render(request,"app/product.html",context)

def CartView(request):
    if request.method == 'POST':
        note = request.POST.get("note", "").strip()
        terms = request.POST.get("terms") == 'on'

        if not terms:
            messages.error(request, "You must agree to the terms and conditions.")
            return redirect("cart")

        # Update all cart items for the user
        cart_items = CartItem.objects.filter(user=request.user)

        # --- Check if cart is empty ---
        if not cart_items.exists():
            messages.error(request, "Your cart is empty. Please add items before checkout.")
            return redirect("cart")

        # If cart is not empty, proceed to save the note/terms
        for cart_item in cart_items:
            cart_item.note = note
            cart_item.terms_accepted = terms
            cart_item.save()

        # Now that everything is saved, redirect to checkout
        return redirect("checkout")

    # Normal GET request to display the cart
    cart_items = CartItem.objects.filter(user=request.user)
    for item in cart_items:
        # Add a subtotal attribute to each item
        item.subtotal = item.product.price * item.quantity

    total_price = sum(item.subtotal for item in cart_items)

    context = {
        "cart_items": cart_items,
        "total_price": total_price,
    }
    return render(request, "app/cart.html", context)


def RemoveCartItem(request, item_id):
    # Get the cart item for the current user
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)

    # Remove the cart item
    cart_item.delete()

    # Optionally, add a success message
    messages.success(request, "Item removed from the cart.")

    # Redirect back to the cart page
    return redirect("cart")

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




def Checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    payment_form=PaymentForm()
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        payment_form = PaymentForm(request.POST)
        if form.is_valid() and payment_form.is_valid():
            # Save checkout details
            checkout = form.save(commit=False)
            checkout.user = request.user
            checkout.save()

            # Create the Order object
            order = Order.objects.create(
                user=request.user,
                first_name=checkout.first_name,
                last_name=checkout.last_name,
                email=checkout.email,
                phone_number=checkout.phone_number,
                address=checkout.address,
                apartment=checkout.appartment,  # notice 'apartment' in Order model
                city=checkout.city,
                postal_code=checkout.postal_code,
                country=checkout.country,
                state=checkout.state,
                notes=checkout.notes,
                terms_accepted=False,  # or handle from form if you like
                total_price=0,         # we will calculate later
            )

            payment = payment_form.save(commit=False)
            payment.order = order
            payment.save()

            # Get all cart items for this user
            cart_items = CartItem.objects.filter(user=request.user)

            # Create OrderItems from the CartItems
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price,
                    color=item.color,
                    size=item.size,
                )

            # Calculate total price in the Order and save
            order.calculate_total_price()

            # Clear the cart
            cart_items.delete()

            messages.success(request, 'Your order has been placed successfully!')
            return redirect('order_confirmation')
        else:
            messages.error(request, 'Please fill in all the required fields.')
            return redirect('checkout')
    else:
        form = CheckoutForm()

    # --- Pass cart items and totals into the context so you can display them ---
    cart_items = CartItem.objects.filter(user=request.user)
    for cart_item in cart_items:
        cart_item.subtotal = cart_item.quantity * cart_item.product.price

    # Example of computing subtotal + shipping:
    shipping_cost = 50
    subtotal = sum(item.product.price * item.quantity for item in cart_items)
    grand_total = subtotal + shipping_cost

    context = {

        'payment_form': payment_form,
        'form': form,
        'cart_items': cart_items,
        'subtotal': subtotal,
        'shipping_cost': shipping_cost,
        'grand_total': grand_total,
    }

    return render(request, 'app/checkout.html', context)

# views.py

def FAQ(request):
    
    faq=FAQs.objects.all()
    context={"faq":faq}
    return render(request, 'app/Faqs.html', context)

def AboutUs(request):
    context={}
    return render(request, 'app/aboutus.html', context)

def order_confirmation(request):
    return render(request, 'app/thanks.html')


def mini_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)    
    context={'cart_items':cart_items}
    return render(request,"templates/base.html",context)

def Not_found_Error(request):
    context={}
    return render(request,"app/404.html",context)

def Comming_Soon(request):
    context={}
    return render(request,"app/comming_soon.html",context)

def Blog(request):
    context={}
    return render(request,"app/blog.html",context)




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