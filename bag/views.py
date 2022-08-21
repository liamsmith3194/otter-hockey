from django.shortcuts import render, redirect, reverse,\
    HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product
# Create your views here.


def view_bag(request):
    """ A view to display the basket page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Adds the product to the basket along with size and quantity """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(
                    request, f'Updated size {size.upper()} {product.name} quantity to \
                        {bag[item_id]["items_by_size"][size]}')
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request, f'Added size {size.upper()} {product.name} \
                        to your basket')
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
                request, f'Added size {size.upper()} {product.name} \
                    to your basket')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} \
                to your basket')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the products updating the subtotal"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    stick_size = None
    clothes_size = None
    if 'stick_size' in request.POST:
        stick_size = request.POST['stick_size']
    bag = request.session.get('bag', {})

    if stick_size:
        if quantity > 0:
            bag[item_id]['items_by_size'][stick_size] = quantity
            messages.success(
                request, f'Updated size {stick_size.upper()} {product.name} \
                    quantity to {bag[item_id]["items_by_size"][stick_size]}')
        else:
            del bag[item_id]['items_by_size'][stick_size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(
                request, f'Removed size {stick_size.upper()} {product.name} \
                    from your basket')

    else:
        if 'clothes_size' in request.POST:
            clothes_size = request.POST['clothes_size']
    bag = request.session.get('bag', {})

    if clothes_size:
        if quantity > 0:
            bag[item_id]['items_by_size'][clothes_size] = quantity
            messages.success(
                request, f'Updated size {clothes_size.upper()} {product.name} \
                    quantity to {bag[item_id]["items_by_size"][clothes_size]}')
        else:
            del bag[item_id]['items_by_size'][clothes_size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(
                request, f'Removed size {clothes_size.upper()} {product.name} \
                    from your basket')

    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} \
                from your basket')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove any product from the basket"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(
                request, f'Removed size {size.upper()} {product.name} \
                    from your basket')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} \
                from your basket')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
