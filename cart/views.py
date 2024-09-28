from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_cart(request):
    """ A view to check shopping cart contents """

    return render(request, 'cart/cart.html')

def add_to_cart(request, product_id):
    """ Add a quantity of the specified product to the shopping cart """

    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if product_id in list(cart.keys()):
        cart[product_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {cart[product_id]}')

    else:
        cart[product_id] = quantity
        messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)    

def adjust_cart(request, product_id):
    """ adjust the the shopping cart amount"""
    
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        del cart[product_id]

    if product_id in list(cart.keys()):
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to {cart[product_id]}')


    request.session['cart'] = cart
    return redirect(reverse('view_cart'))  

def remove_from_cart(request, product_id):
    """ remove item from cart"""

    product = get_object_or_404(Product, pk=product_id)

    cart = request.session.get('cart', {})

    del cart[product_id]

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))          
