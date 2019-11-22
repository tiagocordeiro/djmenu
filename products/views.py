from django.shortcuts import render
from django.db.models import Min

from .models import ProductVariation


# Create your views here.
def products_list(request):
    variacoes = ProductVariation.objects.all()
    context = {
        'variacoes': variacoes,
    }
    return render(request, 'products/list.html', context=context)


def two_flavors(request):
    variacoes = ProductVariation.objects.all()
    min_price_broto = ProductVariation.objects.filter(variation__name='Broto').aggregate(Min('price'))
    min_price_grande = ProductVariation.objects.filter(variation__name='Grande').aggregate(Min('price'))
    context = {
        'variacoes': variacoes,
        'min_price_broto': min_price_broto['price__min'],
        'min_price_grande': min_price_grande['price__min']
    }
    return render(request, 'products/sliced.html', context=context)
