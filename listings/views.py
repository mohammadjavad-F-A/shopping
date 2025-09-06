from datetime import timezone, timedelta

from django.shortcuts import render, redirect, get_object_or_404
from main.models import product
from .models import comment, address, CartItem, Order, OrderItem
from datetime import datetime, timezone
def products(request, id):
    comments =comment.objects.filter(product=id)[:3]

    products = product.objects.get(id=id)
    cat = products.category
    similar_products = product.objects.filter(category__name__icontains=cat)[:2]
    context = {'products': products, 'comments':comments, 'similar_products':similar_products}
    return render(request, 'product.html', context=context)


def more_products(request):
    products = product.objects.all()
    context = {'products': products}
    return render(request, 'search.html', context=context)

def comments(request):
    if request.method == 'POST':
        star = request.POST['star']
        username = request.POST['username']
        id = int(request.POST['id'])
        text = request.POST['text']

        com = comment.objects.create(
            product=id,
            star=star,
            user_name=username,
            content=text,
        )
        com.save()
        return redirect("products", id)
    return render(request, 'product.html')

def addresss(request):
    if request.user.is_authenticated:
        if request.method == 'POST':


            username = request.POST['username']
            userid = request.POST['userid']
            city = request.POST['city']
            district = request.POST['district']
            street = request.POST['street']
            alley = request.POST['alley']
            plaque = request.POST['plaque']
            floor = request.POST['floor']
            unit = request.POST['unit']
            postal = request.POST['postal']
            Address = address(

                user_name=username,
                user_id=userid,
                city=city,
                district=district,
                street=street,
                alley=alley,
                plaque=plaque,
                floor=floor,
                unit=unit,
                postal=postal,
                )
            Address.save()
            return redirect("address")


        Address = address.objects.filter(user_id=request.user.id)
        context = {'Address': Address}
        return render(request, 'address.html', context=context)
    return render(request, 'address.html')




def delete_comment(request, pk, id):
    comments = get_object_or_404(comment, id=id)
    comments.delete()
    return redirect('products', pk)



def change_addresss(request, id):
    if request.user.is_authenticated:
        Address = address.objects.get(id=id)
        if request.method == 'POST':
            Address.user_name = request.user.username
            Address.user_id = request.user.id
            Address.city = request.POST['city']
            Address.district = request.POST['district']
            Address.street = request.POST['street']
            Address.alley = request.POST['alley']
            Address.plaque = request.POST['plaque']
            Address.floor = request.POST['floor']
            Address.unit = request.POST['unit']
            Address.postal = request.POST['postal']
            Address.save()
        context = {'Address': Address}

        return render(request, 'change_address.html', context=context)
    return render(request, 'change_address.html')

def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        return redirect('login')
    products = get_object_or_404(product, id=product_id)

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=products,
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        return redirect('cart')
    return redirect('cart')

def cart_details(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    context = {'cart_items': cart_items, 'total_price': total_price}
    return render(request, 'cart.html', context=context)

def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    count = cart_items.count()
    if request.method == 'POST':
        city = request.POST['city']
        district = request.POST['district']
        street = request.POST['street']
        alley = request.POST['alley']
        plaque = request.POST['plaque']
        floor = request.POST['floor']
        unit = request.POST['unit']
        postal = request.POST['postal']
        order = Order.objects.create(user=request.user, city=city, district=district, street=street, alley=alley, plaque=plaque, floor=floor, unit=unit, postal=postal)
        for item in cart_items:
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)

        cart_items.delete()
        return redirect('peyment', order.id)

    return render(request, 'checkout.html', {'cart_items': cart_items, 'count': count})

def delete_cart(request, id):
    cart = CartItem.objects.get(id=id)
    cart.delete()
    return redirect('cart')

def peyment(request, id):
    peyment = Order.objects.get(id=id)
    context = {'peyment': peyment}
    return render(request, 'payment.html', context=context)

def my_orders(request):
    my_orders = OrderItem.objects.filter(order__user=request.user)
    context = {'my_orders': my_orders}
    return render(request, 'orders.html', context=context)


def delete_auto(request):
    two_days = timezone.now() - timedelta(days=2)
    OrderItem.objects.filter(stat=request.user).delete()



