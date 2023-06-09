"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from products.views import *

app_name = 'products'


urlpatterns = [
    path('', products, name='index'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),  # ../products/baskets/add/<product_id>
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
    path('category/<int:category_id>', products, name='category'),
    path('page/<int:page_number>', products, name='paginator'),
]


