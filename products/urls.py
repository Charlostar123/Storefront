# products/urls.py
# products/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product-list'),
    path('<int:id>/', views.product_detail, name='product-detail'),
    path('cart/add/<int:id>/', views.add_to_cart, name='add-to-cart'),
    path('cart/remove/<int:id>/', views.remove_from_cart, name='remove-from-cart'),
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout_view, name='checkout'),
]
