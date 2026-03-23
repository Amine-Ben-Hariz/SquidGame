from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Count, Q
from django.views import View
from django.contrib import messages
from . forms import CustomerProfileForm, CustomerRegistrationForm
from . models import Cart, Customer, Product, Wishlist, Contact, OrderPlaced
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect
from .forms import ProductForm
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import HttpResponseForbidden
from django.http import HttpResponseNotAllowed
from django.http import HttpResponse
@login_required
def AddProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin1')  # ou autre nom de vue
    else:
        form = ProductForm()
    return render(request, 'app/AddProduct.html', {'form': form})

class AdminProductCreateView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser  # ou un autre critère d'admin

    def get(self, request):
        form = ProductForm()
        return render(request, 'app/admin1.html', {'form': form})

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin1')  # ou afficher un message de succès
        return render(request, 'app/admin1.html', {'form': form})
    
class CustomLoginView(LoginView):
    template_name = 'app/login.html'

    def get_success_url(self):
        print("User connecté :", self.request.user.username, " - ID:", self.request.user.id)
        if self.request.user.id == 50:
            return reverse_lazy('admin1')
        return reverse_lazy('home')
    
def is_user_35(user):
    return user.id == 50

# Solution 1: Avec method_decorator
@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_user_35, login_url='/'), name='dispatch')
class Admin1View(View):
    def get(self, request):
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, "app/admin1.html", locals())
    


# Create your views here.
def home(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request,"app/home.html",locals())

def about(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request,"app/about.html",locals())

def contact(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact.name=name
        contact.email=email
        contact.message=message
        contact.save()
        
    
    return render(request,"app/contact.html",locals())
class CategoryView(View):
    def get(self, request, val):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')

        return render(request, "app/category.html", locals())

class Category_View(View):
    def get(self, request, val):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, "category1.html", locals())

from django.shortcuts import get_object_or_404




class CategoryTitle(View):
    def get(self,request,val):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
           totalitem = len(Cart.objects.filter(user=request.user))
           wishitem = len(Wishlist.objects.filter(user=request.user))
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request,"app/category.html",locals())

  
class ProductDetail(View):  
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        item_already_in_cart = False
        if request.user.is_authenticated: 
         item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
         wishlist = Wishlist.objects.filter(Q(product=product) & Q(user=request.user))
         totalitem = 0
         wishitem = 0
         totalitem = len(Cart.objects.filter(user=request.user))
         wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request,"app/productdetail.html",locals())
    
class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
           totalitem = len(Cart.objects.filter(user=request.user))
           wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request,"app/customerregistration.html",locals())
    def post (self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! User Register Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, "app/customerregistration.html", locals())

@method_decorator(login_required, name='dispatch')    
class ProfileView(View):    
    def get(self,request):
        form = CustomerProfileForm()
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
           totalitem = len(Cart.objects.filter(user=request.user))
           wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, "app/profile.html", locals())
    def post (self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid ():
            user = request.user
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            Governorate = form.cleaned_data['Governorate']
            zipcode = form.cleaned_data['zipcode']
            
            reg = Customer(user=user, name=name, age=age, mobile=mobile, city=city, Governorate=Governorate, zipcode=zipcode)
            reg.save()
            messages.success(request, "Congratulations! Profile Save Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, "app/profile.html", locals())

@login_required
def address(request):
    add = Customer.objects.filter(user=request.user)
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
           totalitem = len(Cart.objects.filter(user=request.user))
           wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, "app/address.html", locals())

@method_decorator(login_required, name='dispatch')
class updateAddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
           totalitem = len(Cart.objects.filter(user=request.user))
           wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, "app/updateAddress.html", locals())
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid ():
            add = Customer.objects.get (pk=pk)
            add.name = form.cleaned_data['name']
            add.age = form.cleaned_data['age']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.Governorate = form.cleaned_data['Governorate']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success (request, "Congratulations! Profile Update Successfully")
        else:
            messages.warning (request, "Invalid Input Data")
        return redirect("address")

@login_required
def add_to_cart(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect("/cart")


@login_required
def orders(request):
    order_placed = OrderPlaced.objects.filter(user=request.user)
    return render(request, "app/orders.html", locals())

@login_required
def show_cart(request):
    user=request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        price = p.product.discounted_price if p.product.discounted_price is not None else p.product.selling_price
        value = p.quantity * price
        amount = amount + value
    totalamount = amount + 7
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
           totalitem = len(Cart.objects.filter(user=request.user))
           wishitem = len(Wishlist.objects.filter(user=request.user))    
    return render(request, "app/addtocart.html", locals())

@login_required
def show_wishlist(request):
    user = request.user
    totalitem= 0
    wishitem=0
    if request.user.is_authenticated:
       totalitem = len(Cart.objects.filter(user=request.user))
       wishitem = len(Wishlist.objects.filter(user=request.user))  
    product = Wishlist.objects.filter(user=user)
    return render(request, "app/wishlist.html",locals())      

@method_decorator(login_required, name='dispatch')
class checkout(View):
    def get(self,request):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
           totalitem = len(Cart.objects.filter(user=request.user))
           wishitem = len(Wishlist.objects.filter(user=request.user))
        user=request.user
        add=Customer.objects.filter(user=user)
        cart_items=Cart.objects.filter(user=user)
        famount = 0
        for p in cart_items:
            price = p.product.discounted_price if p.product.discounted_price is not None else p.product.selling_price
            value = p.quantity * price
            famount = famount + value
        totalamount = famount + 7    
        no_address = (add.count() == 0)
        return render(request, "app/checkout.html", {**locals(), 'no_address': no_address})
    
@login_required 


def payment_done(request):
    if request.method == "POST":
        custid = request.POST.get('custid')
        customer = Customer.objects.get(id=custid)
        cart = Cart.objects.filter(user=request.user)
        for c in cart:
            OrderPlaced.objects.create(
                user=request.user,
                customer=customer,
                product=c.product,
                quantity=c.quantity
            )
            c.delete()
        return render(request, 'app/paymentdone.html')  # <= assure-toi de ce retour
    else:
        return HttpResponseNotAllowed(['POST'])

  
    
       

@login_required 
def plus_cart(request):
    if request.method == 'GET':
        try:
            prod_id = request.GET['prod_id']
            cart_item = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
            product = cart_item.product
            
            if cart_item.quantity < product.stock:
                cart_item.quantity += 1
                cart_item.save()
                
                user = request.user
                cart = Cart.objects.filter(user=user)
                amount = 0
                for p in cart:
                    price = p.product.discounted_price if p.product.discounted_price is not None else p.product.selling_price
                    value = p.quantity * price
                    amount = amount + value
                totalamount = amount + 7
                
                data = {
                    'quantity': cart_item.quantity,
                    'amount': amount,
                    'totalamount': totalamount,
                    'message': 'Quantity updated'
                }
            else:
                data = {
                    'error': 'Stock limit reached',
                    'quantity': cart_item.quantity,
                    'stock': product.stock
                }
                
        except Cart.DoesNotExist:
            data = {'error': 'Cart item not found'}
        except Exception as e:
            data = {'error': str(e)}
        
        return JsonResponse(data)


@login_required
def minus_cart(request):
    if request.method == 'GET':
       prod_id=request.GET['prod_id']
       c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
       c.quantity-=1
       c.save()
       user=request.user
       cart = Cart.objects.filter(user=user)
       amount = 0
       for p in cart:
           price = p.product.discounted_price if p.product.discounted_price is not None else p.product.selling_price
           value = p.quantity * price
           amount = amount + value
       totalamount = amount + 7
       data={
        'quantity':c.quantity,
        'amount': amount,
        'totalamount': totalamount
       }
    return JsonResponse(data)

@login_required
def remove_cart(request):
    if request.method == 'POST':
        try:
            prod_id = request.POST.get('prod_id')
            if not prod_id:
                return JsonResponse({'error': 'Product ID is required'}, status=400)
            
            Cart.objects.filter(Q(product=prod_id) & Q(user=request.user)).delete()
            
            user = request.user
            cart = Cart.objects.filter(user=user)
            amount = 0
            for p in cart:
                price = p.product.discounted_price if p.product.discounted_price is not None else p.product.selling_price
                value = p.quantity * price
                amount += value
            totalamount = amount + 7
            
            data = {
                'amount': amount,
                'totalamount': totalamount,
                'message': 'Item(s) removed successfully'
            }
            return JsonResponse(data)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

            
  

@login_required
def plus_wishlist(request):
    if request.method == 'GET':
       prod_id=request.GET['prod_id']
       product=Product.objects.get(id=prod_id)
       user = request.user
       Wishlist(user=user,product=product).save()
       data={
           'message': 'Wishlist Added Successfully',
       }
    return JsonResponse(data)

@login_required   
def minus_wishlist(request):
    if request.method == 'GET':
       prod_id=request.GET['prod_id']
       product=Product.objects.get(id=prod_id)
       user = request.user
       Wishlist.objects.filter(user=user,product=product).delete()
       data={
           'message': 'Wishlist Remove Successfully',
       }
    return JsonResponse(data)   

def search(request):
    query = request.GET['search']
    totalitem= 0
    wishitem=0
    if request.user.is_authenticated:
       totalitem = len(Cart.objects.filter (user=request.user))
       wishitem = len(Wishlist.objects.filter (user=request.user))
    product = Product.objects.filter(Q(title__icontains=query))
    return render(request, "app/search.html", locals())

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect(request.META.get('HTTP_REFERER', 'product-list'))

from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages


def deleteAddress(request, pk):
    if request.method == 'POST':
        address = get_object_or_404(Customer, id=pk, user=request.user)
        address.delete()
        messages.success(request, "Address deleted successfully!")
    return redirect('address')

@login_required
def addAddress(request):
    if request.method == 'POST':
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            Governorate = form.cleaned_data['Governorate']
            zipcode = form.cleaned_data['zipcode']
            
            reg = Customer(user=user, name=name, age=age, mobile=mobile, city=city, Governorate=Governorate, zipcode=zipcode)
            reg.save()
            messages.success(request, "Address added successfully!")
            return redirect('address')
    else:
        form = CustomerProfileForm()
    return render(request, "app/profile.html", locals())

@login_required
def delete_delivered_order(request, order_id):
    order = get_object_or_404(OrderPlaced, id=order_id, user=request.user)
    if order.status == 'Delivered':
        order.delete()
        messages.success(request, "Order deleted successfully!")
    else:
        messages.error(request, "Only delivered orders can be deleted!")
    return redirect('orders')

@login_required
def cancel_order(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(OrderPlaced, id=order_id, user=request.user)
        if order.status not in ['Delivered', 'Cancelled']:
            order.status = 'Cancelled'
            order.save()
    return redirect('orders')
