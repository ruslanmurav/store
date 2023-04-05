from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from products.models import ProductCategory, Product, Basket
from django.views.generic import TemplateView
from users.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


class IndexView(TemplateView):
    template_name = 'products/index.html'



# Create your views here.
def products(request, category_id=None, page_number=1):
    if category_id is not None:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    per_page = 3
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_number)
    context = {
        'title': 'Store - products',
        'products': products_paginator,
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products\products.html', context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])