from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add-to-cart/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('your-cart/', views.your_cart, name='your_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/success', views.checkout_success, name='checkout_success'),
]


