from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Q487N2MlNpuuhu1yBBzd2sDOzHIvv5QtEab7FX2L1w72w6oN4kDRnt5w3YCwt1McH3T8rwk49fog3lJxXbHG8WV006RYGS1N1',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)