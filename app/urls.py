from django.urls import path , include
from . import views

urlpatterns = [
    path("",views.Homepage,name="home"),
    path("shop",views.shoppage,name="shop"),
    path("product/<slug:slug>",views.Product,name="product"),
    path('add-to-cart/', views.AddToCart, name='add_to_cart'),
    path('update-cart-item/', views.update_cart_item, name='update_cart_item'),
    path("cart",views.CartView,name="cart"),
    path("checkout",views.Checkout,name="checkout"),
    path("aboutus",views.AboutUs,name="aboutus"),
    path("contactus",views.Contactus,name="contactus"),
    path("404",views.Not_found_Error,name="404"),
    path("commingsoon",views.Comming_Soon,name="Coming_Soon"),
    path("blog",views.Blog,name="blog"),
    path("accounts/register",views.Register,name="register"),
    path("wishlist",views.Wishlist,name="wishlist"),
    path('thankyou/', views.order_confirmation, name='order_confirmation'),
    
]
