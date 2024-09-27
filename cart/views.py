from django.shortcuts import render, redirect, reverse

# Create your views here.

def view_cart(request):
    """ A view to check shopping cart contents """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)    

def adjust_cart(request, item_id):
    """ adjust the the shopping cart amount"""

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        del cart[item_id]

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))  

def remove_from_cart(request, item_id):
    """ remove item from cart"""

    cart = request.session.get('cart', {})

    if quantity > 0:
        del cart[item_id]

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))          