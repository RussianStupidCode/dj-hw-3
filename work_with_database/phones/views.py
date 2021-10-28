from django.http import Http404
from django.shortcuts import render, redirect

from phones.models import Phone

SORT_REQUEST_MAP = {
    'name': 'name',
    'min_price': 'price',
    'max_price': '-price'
}


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()

    sort_flag = request.GET.get('sort')
    if sort_flag:
        phones = phones.order_by(SORT_REQUEST_MAP[sort_flag])

    context = {
        'phones': phones
    }

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'

    try:
        phone = Phone.objects.get(slug=slug)
    except:
        raise Http404("Phone not exist")

    context = {'phone': phone}
    return render(request, template, context)
