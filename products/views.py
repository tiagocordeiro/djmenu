from django.shortcuts import render

from .models import ProductCategory, ProductVariation, ProductIngredient


# Create your views here.
def products_list(request):
    bebidas = ProductCategory.objects.filter(category__name='Bebidas')
    variacoes = ProductVariation.objects.all()
    ingredientes = ProductIngredient.objects.all()
    context = {
        'bebidas': bebidas,
        'variacoes': variacoes,
        'ingredientes': ingredientes,
    }
    return render(request, 'products/list.html', context=context)
