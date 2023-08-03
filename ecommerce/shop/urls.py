from django.urls import path
from shop.views import index,detail
from . import views

urlpatterns = [
    path('', index, name='Home'),
    path('<int:myid>', detail, name='Detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('view-cart/', views.view_cart, name='view_cart'),
    path('update-cart/<int:cart_item_id>/', views.update_cart, name='update_cart'),
    path('remove-from-cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('produits/', views.produits_view, name='produits'),
]




