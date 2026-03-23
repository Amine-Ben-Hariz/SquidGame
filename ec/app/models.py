from typing import Self
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

CATEGORY_CHOICES = (
    ('Mo', 'Monitors'),
    ('CA', 'Camera'),
    ('Ke', 'Keyboards'),
    ('Ms', 'Mouses'),
    ('He', 'Headsets'),
    ('Mp', 'Mousepads'),
    ('Jo', 'Joysticks'),
    ('Mi', 'Microphones'),
    ('Sp', 'Speekers'),
)

GOVERNORATE_CHOICES = (
    ('Ariana', 'Ariana'), ('Béja', 'Béja'),
    ('Ben Arous', 'Ben Arous'), ('Bizerte', 'Bizerte'),
    ('Gabès', 'Gabès'), ('Gafsa', 'Gafsa'),
    ('Jendouba', 'Jendouba'), ('Kairouan', 'Kairouan'),
    ('Kasserine', 'Kasserine'), ('Kebili', 'Kebili'),
    ('Kef', 'Kef'), ('Mahdia', 'Mahdia'),
    ('Manouba', 'Manouba'), ('Medenine', 'Medenine'),
    ('Monastir', 'Monastir'), ('Nabeul', 'Nabeul'),
    ('Sfax', 'Sfax'), ('Sidi Bouzid', 'Sidi Bouzid'),
    ('Siliana', 'Siliana'), ('Sousse', 'Sousse'),
    ('Tataouine', 'Tataouine'), ('Tozeur', 'Tozeur'),
    ('Tunis', 'Tunis'), ('Zaghouan', 'Zaghouan'),
)



class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField(null=True, blank=True)
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
    stock = models.PositiveIntegerField(default=0)

    @property
    def stock_status(self):
        return "Hors stock" if self.stock == 0 else "En stock"

    def __str__(self):
        return str(self.id)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    Governorate = models.CharField(choices=GOVERNORATE_CHOICES, max_length=100)

    def _str_(self):
        return str(Self.id)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def _str_(self):
        return str(Self.id)

    @property
    def total_cost(self):
        price = self.product.discounted_price if self.product.discounted_price is not None else self.product.selling_price
        return self.quantity * price


STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel')
)


class OrderPlaced (models.Model):
    user = models. ForeignKey(User, on_delete=models.CASCADE)
    customer = models. ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default='Pending')

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
