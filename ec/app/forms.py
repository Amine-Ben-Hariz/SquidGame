from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, SetPasswordForm, PasswordResetForm
from django import forms
from .models import Product
from .models import Customer

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'selling_price', 'discounted_price', 'description', 'category', 'product_image', 'stock']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'product_image': forms.FileInput(),
            'stock': forms.NumberInput(attrs={'min': 0})
        }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus ': 'True','class': 'form-control' }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}))

class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus ':'True','class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password ', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm password ', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
class MyPasswordChangeForm (PasswordChangeForm):
    old_password = forms.CharField (label='Old Password', widget=forms.PasswordInput (attrs={'autofocus ': 'True', 'autocomplete': 'current-password', 'class': 'form-control'}))
    new_password1 = forms.CharField (label='New Password', widget=forms.PasswordInput (attrs={'autocomplete': 'current-password', 'class': 'form-control'}))
    new_password2 = forms.CharField (label='Confirm Password', widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}))
        
class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

class MySetPasswordForm (SetPasswordForm):
    new_password1 = forms.CharField (label='New Password', widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}))
    new_password2 = forms.CharField (label='Confirm New Password', widget=forms.PasswordInput (attrs={'autocomplete': 'current-password', 'class': 'form-control'}))

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','age','city','mobile','Governorate','zipcode']
        widgets={
            'name': forms.TextInput(attrs={ 'class': 'form-control' }),
            'age': forms.NumberInput(attrs={'class': 'form-control' }),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput (attrs={'class': 'form-control' }),
            'Governorate': forms.Select (attrs={'class': 'form-control'}),
            'zipcode': forms.NumberInput(attrs={'class': 'form-control' }),}
