from django import forms

import django.db
import django.db.models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from app.models import Subscribe, Review,Messages ,Checkout


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields ='__all__'
        labels={'email':_('')}

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder']='Enter Your Email'


class User_Reg(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter First Name'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter Last Name'}))

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder']='Enter User Name '
        self.fields['first_name'].widget.attrs['placeholder']='Enter First Name ' 
        self.fields['last_name'].widget.attrs['placeholder']='Enter Last Name '  
        self.fields['email'].widget.attrs['placeholder']='Enter Email ' 
        self.fields['password1'].widget.attrs['placeholder']='Enter Password ' 
        self.fields['password2'].widget.attrs['placeholder']='Confirm Password ' 
    
    def clean_username(self):
        username=self.cleaned_data['username'].lower()
        new = User.objects.filter(username=username)
        if new.count():
            raise forms.ValidationError("Username Already Exists!")
        return username
    
    def clean_email(self):
        email=self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise forms.ValidationError("User on Email Already Exists!")
        return email
    
    def clean_password2(self):
        password1=self.cleaned_data['password1']
        password2=self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords Doesn't Match")
        return password2
    


class PriceFilterForm(forms.Form):
    min_price = forms.IntegerField(required=False, min_value=0, widget=forms.NumberInput(attrs={
        'placeholder': 'Min Price',
        'class': 'form-control',
        'id': 'id_min_price'
    }))
    max_price = forms.IntegerField(required=False, min_value=0, widget=forms.NumberInput(attrs={
        'placeholder': 'Max Price',
        'class': 'form-control',
        'id': 'id_max_price'
    }))

    def clean(self):
        cleaned_data = super().clean()
        min_price = cleaned_data.get("min_price")
        max_price = cleaned_data.get("max_price")

        if min_price and max_price:
            if min_price > max_price:
                raise forms.ValidationError("Min price cannot be greater than Max price.")
    
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields ={"name",'email','title',"comment"}

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder']='e.g Awais Ali' 
        self.fields['email'].widget.attrs['placeholder']='e.g xyz@gmail.com'
        # self.fields['rating'].widget.attrs['placeholder']='Email'
        self.fields['title'].widget.attrs['placeholder']='e.g Perfect Product'
        self.fields['comment'].widget.attrs['placeholder']='e.g bla bla bla ....'

class MessageForm(forms.ModelForm):
    class Meta:
        model=Messages
        fields={"name","email","phone_number","message"}
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder']='e.g Awais Ali' 
        self.fields['email'].widget.attrs['placeholder']='e.g xyz@gmail.com'
        # self.fields['rating'].widget.attrs['placeholder']='Email'
        self.fields['phone_number'].widget.attrs['placeholder']='+923********* ( Optional )'
        self.fields['message'].widget.attrs['placeholder']='e.g Can I get more info about this Product'

     
class CheckoutForm(forms.ModelForm):
    class Meta:
        model=Checkout
        fields={"first_name","last_name","email","phone_number","address","appartment","city","postal_code","country","state","notes"}
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder']='e.g Awais Ali' 
        self.fields['last_name'].widget.attrs['placeholder']='e.g Awais Ali'
        self.fields['email'].widget.attrs['placeholder']='e.g Awais Ali'
        self.fields['phone_number'].widget.attrs['placeholder']='e.g Awais Ali'
        self.fields['address'].widget.attrs['placeholder']='e.g Awais Ali'
        self.fields['appartment'].widget.attrs['placeholder']='e.g Awais Ali'
        self.fields['city'].widget.attrs['placeholder']='e.g Awais Ali'
        self.fields['postal_code'].widget.attrs['placeholder']='e.g Awais Ali'
        self.fields['country'].widget.attrs['placeholder']='e.g Awais Ali'
        self.fields['state'].widget.attrs['placeholder']='e.g Awais Ali'
        self.fields['notes'].widget.attrs['placeholder']='e.g Awais Ali'
        self.fields['country'].widget.attrs['placeholder']='e.g Awais Ali'
    