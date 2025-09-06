from django.urls import path
from .views import *
urlpatterns = [

    path('product/<int:id>', products, name='products'),
    path('more_products/', more_products, name='more_products'),
    path('comments/', comments, name='comments'),
    path('address/', addresss, name='address'),
    path('product/<int:pk>/comment/<int:id>/delete/', delete_comment, name='delete'),
    path('change_address/<int:id>', change_addresss, name='change_address'),
    path('add_to_cart//<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_details, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('delete_cart<int:id>/', delete_cart, name='delete_cart'),
    path('peyment/<int:id>/', peyment, name='peyment'),
    path("my_orders/", my_orders, name="my_orders"),
]