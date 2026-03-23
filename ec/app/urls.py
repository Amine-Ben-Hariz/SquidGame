from django.urls import path
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .views import CustomLoginView, Admin1View
from .forms import LoginForm
from .views import AdminProductCreateView
from .views import delete_product
from .views import Category_View
from django.urls import path, re_path
from django.views.generic.base import RedirectView
from .views import deleteAddress

urlpatterns = [
  path('delete-address/<int:pk>/', deleteAddress, name='deleteAddress'),
  path('add-address/', views.addAddress, name='addAddress'),
  path('paymentdone/', views.payment_done, name='paymentdone'),
  re_path(r'^paymentdone$', RedirectView.as_view(url='/paymentdone/', permanent=True)),
  path("category1/<slug:val>", views.Category_View.as_view(),name="category1"),
  path('delete-product/<int:id>/', delete_product, name='delete_product'),
  path('AddProduct/', views.AddProduct, name='addproduct'),
  path('admin1/', AdminProductCreateView.as_view(), name='admin1'),
  path("", views.home, name="home"),  # Make sure this exists
  path("contact/", views.contact),
  path("about/", views.about),
  path("category/<slug:val>", views.CategoryView.as_view(),name="category"),
  path("category-title/<int:pk>", views.CategoryTitle.as_view(),name="category-title"),
  path("product-detail/<int:pk>", views.ProductDetail.as_view(),name="product-detail"),
  path('profile/', views.ProfileView.as_view(), name='profile'),
  path('address/', views.address, name='address'),
  path('updateAddress/<int:pk>', views.updateAddress.as_view(), name='updateAddress'),
  
  path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
  path('cart/', views.show_cart, name='showcart'),
  path('checkout/', views.checkout.as_view(), name='checkout'),
  path('paymentdone/', views.payment_done),
  path('orders/', views.orders, name='orders'),
  path('delete-delivered-order/<int:order_id>/', views.delete_delivered_order, name='delete_delivered_order'),
  path('cancel-order/<int:order_id>/', views.cancel_order, name='cancel_order'),
  
  path('search/', views.search, name='search'),
  path('wishlist/', views.show_wishlist, name='showwishlist'),
  path('wishlist/remove/<int:prod_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
  
  path('pluscart/', views.plus_cart),
  path('minuscart/', views.minus_cart),
  path('removecart/', views.remove_cart, name='removecart'),
  path('pluswishlist/', views.plus_wishlist),
  path('minuswishlist/', views.minus_wishlist),
  
  #login authentification
  path("registration/", views.CustomerRegistrationView.as_view(),name="customerregistration"),
  path("accounts/login/", CustomLoginView.as_view(template_name="app/login.html", authentication_form=LoginForm), name="login"),
  path('admin1/', Admin1View.as_view(), name='admin1'),
  path("passwordchange/", auth_view.PasswordChangeView.as_view(template_name="app/changepassword.html", form_class=MyPasswordChangeForm, success_url="/passwordchangedone"),name="passwordchange"),
  path("passwordchangedone/", auth_view.PasswordChangeView.as_view(template_name="app/passwordchangedone.html", form_class=MyPasswordChangeForm, success_url='/passwordchangedone'),name="passwordchangedone"),
  path("logout/", auth_view.LogoutView.as_view(),name="logout"),
  
  path('password-reset/', auth_view.PasswordResetView.as_view(
      template_name="app/password_reset.html",
      form_class=MyPasswordResetForm,
      email_template_name="app/password_reset_email.txt",
      html_email_template_name="app/password_reset_email.html",
      subject_template_name="app/password_reset_subject.txt"
  ), name="password_reset"),
  path("password-reset/done/", auth_view.PasswordResetDoneView.as_view(template_name="app/password_reset_done.html"),name="password_reset_done"),
  path("password-reset-confirm/<uidb64>/<token>/", auth_view.PasswordResetConfirmView.as_view(template_name="app/password_reset_confirm.html",form_class=MySetPasswordForm), name="password_reset_confirm"),
  path("password-reset-complete/", auth_view.PasswordResetCompleteView.as_view (template_name="app/password_reset_complete.html"), name="password_reset_complete"),

  
  
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)