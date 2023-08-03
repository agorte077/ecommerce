from django.shortcuts import render
from .models import Product, SearchQuery

# Create your views here.
def index(request):


    products_object=Product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        products_object = Product.objects.filter(title__icontains =item_name )
       

    return render(request, 'shop/index.html', {'product_object': products_object})


def detail(request,myid):
    products_object = Product.objects.get(id=myid)
    return render(request,'shop/detail.html',{'product': products_object})





# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CartItem
from .models import Product

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('Home')

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'shop/cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def update_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
        cart_item.quantity = quantity
        cart_item.save()
    return redirect('view_cart')

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return redirect('view_cart')

from django.shortcuts import render
from django.http import HttpResponse

def produits_view(request):
    # Votre logique pour récupérer les produits depuis la base de données ou autre source de données
    produits = [
        {'nom': 'Produit 1', 'prix': 10},
        {'nom': 'Produit 2', 'prix': 15},
        # Ajoutez ici les autres produits que vous souhaitez afficher
    ]

    # Vous pouvez utiliser un template pour générer le contenu de la page
    context = {'produits': produits}
    return render(request, 'shop/produits.html', context)







