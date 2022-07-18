from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KxaW6DoIR1A4L5uVANtb0wJN8LQko4gD76NyUSJ8YsY1vjtBvngkWJ1cQ3HsWxmLHwqR46oUHEEIO1Uh4dxnBZC00TKDuQayN',
        'client_secret': 'test',
    }

    return render(request, template, context)

def checkout_success(request):
    

    return render(request, 'checkout/checkout_success.html')