from .models import CartItem  # Adjust based on your cart model

def minicart_data(request):
    cart_items = []
    cart_total = 0.0
    total_item=0

    if request.user.is_authenticated:  # Ensure the user is logged in
        user_cart = CartItem.objects.filter(user=request.user)  # Adjust based on your cart model
        total_item=CartItem.objects.filter(user=request.user).count()
        cart_items = user_cart
        cart_total = sum(item.product.price * item.quantity for item in user_cart)

    return {
        'cart_items': cart_items,
        'cart_total': cart_total,
        "total_item":total_item
    }
