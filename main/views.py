from django.shortcuts import render, get_object_or_404
from datetime import datetime

from .models import WishList, Product
from .forms import ProductForm


def index(request):
    return render(request, 'index.html', {"title": "Wishlist | home page"})

def about(request):
    return render(request, 'about.html', {"title": "Wishlist | about project"})

def list_page(request, pk):
    """View page the wishlist"""
    wishlist = get_object_or_404(WishList, pk=pk)

    if request.method=='POST':
        form = ProductForm(request.POST)
        instance_product = form.save()
        wishlist.product.add(instance_product)
        wishlist.save()

    elif request.method=='GET':
        form = ProductForm()

    return render(
        request,
        "wish_list.html",
        {
            'wishlist':wishlist,
            'is_owner_list': wishlist.owner == request.user,
            'form': form,
        }
    )

def all_wish_list(request):
    """All the wishlists view page"""
    wishlist = WishList.objects.all()
    #pk = WishList.get(pk=pk)
    return render(request, "all_wishlists.html", {'wishlist':wishlist,}
)

def product(request, product_id):
    name= Product.objects.filter(id=product_id)
    product_name = Product.objects.all()
    current_product = Product.objects.get(pk = product_id)
    context  = {'name': name, 'product_id': product_id, 'current_product': current_product}
    return render(request, 'index.html', context)