from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


from django.core.validators import MinValueValidator, MaxValueValidator


class Profile(models.Model):
    name=models.OneToOneField(User,max_length=50,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Subscribe(models.Model):
    email=models.EmailField()
    date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class Color(models.Model):
    name = models.CharField(max_length=30, unique=True)
    hex_code = models.CharField(max_length=7, blank=True, null=True)  # Optional: for color display

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=5, unique=True)  # e.g., S, M, L, XL

    def __str__(self):
        return self.name

class Login(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=20)

class Brand(models.Model):
    name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    slug=models.SlugField(max_length=50,unique=True,blank=True)
    in_stock=models.BooleanField()
    stock_quantity=models.IntegerField()
    last_update=models.DateTimeField(auto_now=True)
    sku=models.CharField(max_length=50)
    view_count=models.IntegerField(null=True,blank=True)
    price=models.IntegerField()
    striked_price=models.IntegerField(blank=True,null=True,default=0)
    product_type=models.CharField(max_length=20)
    collections=models.CharField(max_length=50)
    main_image= models.ImageField(upload_to='products/')  # Shown by default
    hover_image= models.ImageField(upload_to='products/')  # Shown on hover
    tag=models.ManyToManyField('Tag',related_name='products',blank=True)
    sizes = models.ManyToManyField(Size, related_name='products', blank=True)
    color = models.ManyToManyField(Color, related_name='productscolor', blank=True)
    brand=models.ForeignKey(Brand, on_delete=models.CASCADE,related_name='brand',blank=True)

 

    def save(self,*args, **kwargs):
        if not self.id:
            self.slug=slugify(self.name)
        return super(Products,self).save(*args, **kwargs)



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"  # Correct singular form
        verbose_name_plural = "Products"  # Correct plural form


class FAQs(models.Model):
    title=models.CharField(max_length=100)
    question=models.CharField(max_length=50)
    answer=models.TextField()

    class Meta:
        verbose_name = "FAQ"  # Correct singular form
        verbose_name_plural = "fAQs"  # Correct plural form

class Review(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Ties the review to a user
    name=models.CharField(max_length=50)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)] , null=True , blank=True
    )  # Star rating, e.g., 1-5
    email=models.EmailField()
    title=models.CharField(max_length=50)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('product', 'user'),)
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.username} - {self.product.name} - {self.rating}'
    

class Tag(models.Model):
    name = models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,unique=True ,blank=True)

    def save(self,*args, **kwargs):
        if not self.id:
            self.slug=slugify(self.name)
        return super(Tag,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class ProductVariants(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='variants')
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

    stock_quantity = models.IntegerField(default=0)

    class Meta:
        unique_together = ('product', 'color', 'size')
        verbose_name = "Product Variant"
        verbose_name_plural = "Product Variants"

    def __str__(self):
        return f"{self.product.name} - {self.color.name} - {self.size.name}"
    

class ProductImage(models.Model):
    variant = models.ForeignKey(ProductVariants, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.variant.product.name} - {self.variant.color.name} Image"
    
class Messages(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='message')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone_number = models.CharField(max_length=13,blank=True,null=True)
    message=models.TextField()

    class Meta:
        verbose_name = "Message"  # Correct singular form
        verbose_name_plural = "Messages"  # Correct plural form

    def __str__(self):
        return f"{self.name} - {self.phone_number}"
    
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    note = models.TextField(blank=True, null=True)  # Optional notes for the cart item
    terms_accepted = models.BooleanField(default=False)  # Terms acceptance status

    # Ensure that the combination of user, product, color, and size is unique
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'product', 'color', 'size'], name='unique_cart_item')
        ]


class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # item=models.ForeignKey(CartItem,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,blank=True,null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=255)
    appartment=models.CharField(max_length=50  , blank=True,null=True)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)  # Optional notes for the order
    # terms_accepted = models.BooleanField(default=False)  # Terms acceptance status
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.created_at}"
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User placing the order
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=255)
    apartment = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)  # Optional notes for the order
    terms_accepted = models.BooleanField(default=False)  # Terms acceptance status
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # Total price of the order
    status = models.CharField(
        max_length=50,
        choices=[
            ('pending', 'Pending'),
            ('processing', 'Processing'),
            ('shipped', 'Shipped'),
            ('delivered', 'Delivered'),
            ('cancelled', 'Cancelled')
        ],
        default='pending'
    )  # Status of the order
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id} by {self.first_name} {self.last_name}"

    # This method calculates the total price for the order from related OrderItems
    def calculate_total_price(self):
        total = sum(item.price * item.quantity for item in self.orderitem_set.all())
        self.total_price = total
        self.save()
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)  # Link to the Order
    product = models.ForeignKey(Products, on_delete=models.CASCADE)  # Link to the Product
    quantity = models.PositiveIntegerField()  # Quantity of the product in the order
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price at the time of order
    color = models.CharField(max_length=100)  # Color selected by the user
    size = models.CharField(max_length=100)  # Size selected by the user

    def __str__(self):
        return f'{self.product.name} - {self.quantity} x {self.price}'
    

class Payment(models.Model):
    PAYMENT_CHOICES = [
        ('bank_transfer', 'Direct Bank Transfer'),
        ('cheque', 'Cheque Payment'),
        ('paypal', 'PayPal'),
        ('card', 'Credit Card'),
    ]

    order = models.OneToOneField(
        'app.Order',  # or wherever your Order model lives
        on_delete=models.CASCADE
    )
    method = models.CharField(max_length=50, choices=PAYMENT_CHOICES, default='bank_transfer')

    # If "Credit Card" is chosen, store these details:
    card_name = models.CharField(max_length=100, blank=True, null=True)
    card_type = models.CharField(max_length=50, blank=True, null=True)  # e.g. Visa, MasterCard
    card_number = models.CharField(max_length=20, blank=True, null=True)
    card_cvv = models.CharField(max_length=4, blank=True, null=True)
    card_expiry = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment #{self.id} for Order {self.order.id}"




# class Comment(models.Model):
#     content=models.TextField()
#     date=models.DateField(auto_now=True)
#     name=models.CharField(max_length=100)
#     email=models.EmailField(max_length=200)
#     website=models.CharField(max_length=200)
#     post=models.ForeignKey(Products,on_delete=models.CASCADE)
#     author=models.ForeignKey(User,on_delete=models.CASCADE, null=True,blank=True)
#     parent=models.ForeignKey('self',on_delete=models.DO_NOTHING ,null=True,blank=True, related_name='replies')
    
#     class Meta:
#         verbose_name = "Comment"  # Correct singular form
#         verbose_name_plural = "Comments"  # Correct plural form

#     def __str__(self):
#         return self.name



