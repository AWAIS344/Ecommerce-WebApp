from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

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
    price=models.IntegerField()
    striked_price=models.IntegerField(blank=True,null=True,default=0)
    product_type=models.CharField(max_length=20)
    collections=models.CharField(max_length=50)
    main_image= models.ImageField(upload_to='products/')  # Shown by default
    hover_image= models.ImageField(upload_to='products/')  # Shown on hover
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


class ProductImage(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')
    alt_text = models.CharField(max_length=255, blank=True, null=True)  # Optional for accessibility
    order = models.IntegerField(default=0)
    


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

    # Ensure that the combination of user, product, color, and size is unique
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'product', 'color', 'size'], name='unique_cart_item')
        ]





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



