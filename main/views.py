from django.shortcuts import render, redirect, get_object_or_404
from .models import category, product
from listings.models import special_products
from django.db.models import Q, F
def index(request):
    special = special_products.objects.filter(is_published=True)
    categories = category.objects.all()
    products = product.objects.filter(is_published=True)[:4]
    context = {'categories': categories, 'products': products, 'special': special}
    return render(request, 'index.html', context=context)

def category_detail(request, slug):
    categorys = get_object_or_404(category, slug=slug)
    products = product.objects.filter(category=categorys)
    return render(request, "category_detail.html", {"categorys": categorys, "products": products})


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        search = product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))
        if not search:
            print("not found")
        else:
            return render(request, "search2.html", {"search": search})
    return render(request, "search2.html", {})


def about(request):
    return render(request, "about.html", {})

