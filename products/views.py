
# products/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

from .models import Order, OrderItem  # make sure this is at the top

def checkout_view(request):
    cart = request.session.get('cart', {})
    product_ids = [int(pid) for pid in cart.keys()]
    products = Product.objects.filter(id__in=product_ids)

    if request.method == 'POST':
        order = Order.objects.create()
        for product in products:
            qty = cart[str(product.id)]
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=qty,
                price=product.price
            )
        request.session['cart'] = {}
        return render(request, 'products/checkout_success.html', {'order': order})

    total = sum(product.price * cart[str(product.id)] for product in products)
    return render(request, 'products/checkout.html', {'cart': cart, 'products': products, 'total': total})
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'products/product_detail.html', {'product': product})

def home_view(request):
    return render(request, 'home.html')

def add_to_cart(request, id):
    cart = request.session.get('cart', {})
    cart[str(id)] = cart.get(str(id), 0) + 1
    request.session['cart'] = cart
    return redirect('cart')

def remove_from_cart(request, id):
    cart = request.session.get('cart', {})
    if str(id) in cart:
        del cart[str(id)]
    request.session['cart'] = cart
    return redirect('cart')

def cart_view(request):
    cart = request.session.get('cart', {})
    product_ids = [int(pid) for pid in cart.keys()]
    products = Product.objects.filter(id__in=product_ids)
    cart_items = []
    total = 0
    for product in products:
        qty = cart[str(product.id)]
        subtotal = product.price * qty
        total += subtotal
        cart_items.append({
            'product': product,
            'quantity': qty,
            'total': subtotal
        })
    return render(request, 'products/cart.html', {'cart_items': cart_items, 'cart_total': total})

def checkout_view(request):
    if request.method == 'POST':
        request.session['cart'] = {}
        return render(request, 'products/checkout_success.html')

    cart = request.session.get('cart', {})
    product_ids = [int(pid) for pid in cart.keys()]
    products = Product.objects.filter(id__in=product_ids)
    total = sum(product.price * cart[str(product.id)] for product in products)
    return render(request, 'products/checkout.html', {'cart': cart, 'products': products, 'total': total})
