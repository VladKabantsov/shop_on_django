from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *
from .forms import ToysFilterForm


def landing(request):
    name = "CodingMedved"
    current_day = "03.01.2017"
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print (request.POST)
        print (form.cleaned_data)
        data  = form.cleaned_data
        print (data["name"])

        new_form = form.save()

    return render(request, 'landing/landing.html', locals())


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_phones = products_images.filter(product__category__id=1)
    products_images_laptops = products_images.filter(product__category__id=2)
    return render(request, 'landing/home.html', locals())


def news(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_phones = products_images.filter(product__category__id=1)
    products_images_laptops = products_images.filter(product__category__id=2)
    return render(request, 'landing/news.html', locals())

def catalog(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    ProductImage.price = getattr(Product, 'price')
    # price = ProductImage()
    # currency_price = price.price_float()
    # print(currency_price)
    form = ToysFilterForm(request.GET)
    if form.is_valid():
        if form.cleaned_data["min_price"]:
            products_images = products_images.filter(price__gte=form.cleaned_data["min_price"], is_active=True,
                                                     is_main=True, product__is_active=True)
            print("Min_ok")
        if form.cleaned_data["max_price"]:
            products_images = products_images.filter(price__lte=form.cleaned_data["max_price"], is_active=True,
                                                     is_main=True, product__is_active=True)
            print("Max_ok")
        if form.cleaned_data["ordering"]:
            products_images = products_images.order_by(form.cleaned_data["ordering"])
    products_images_phones = products_images.filter(product__category__id=1)
    products_images_laptops = products_images.filter(product__category__id=2)
    return render(request, 'landing/catalog.html', locals())
