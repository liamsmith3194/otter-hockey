from django.shortcuts import render, redirect, reverse

# Create your views here.

def view_bag(request):
    """ A view to display the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    clothes_size = None
    if 'clothes_size' in request.POST:
        clothes_size = request.POST['clothes_size']
    bag = request.session.get('bag', {})

    if clothes_size:
        if item_id in list(bag.keys()):
            if clothes_size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][clothes_size] += quantity
            else:
                bag[item_id]['items_by_size'][clothes_size] = quantity
        else:
            bag[item_id] = {'items_by_size': {clothes_size: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
