from django.utils.html import format_html
from django.urls import reverse
from django.contrib import admin
from . models import Cart, Customer,Product, Wishlist, Contact, OrderPlaced
from django.contrib.auth.models import Group

# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','selling_price','discounted_price','category','stock','stock_status','product_image']
    list_filter = ['category']
    search_fields = ['title', 'category']
    list_per_page = 10  # Nombre de produits par page
    
    
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','age','city','mobile','Governorate','zipcode']
    
@admin.register(Cart)
class CartModelAdmin (admin.ModelAdmin):
    list_display=['id', 'user', 'product', 'quantity']
    def products (self, obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>',link, obj.product.title) 

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','customer','product','quantity','ordered_date','status']    
    
@admin.register(Wishlist)   
class WishlistModelAdmin (admin.ModelAdmin):
 list_display = ['id','user','product']
 def products (self, obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>',link, obj.product.title)

@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','message']     
    
admin.site.unregister(Group)
