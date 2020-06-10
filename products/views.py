from django.contrib import messages
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.db.models import Min

from .forms import CategoryForm, ProductForm, VariationForm, \
    ProductVariationForm
from .models import ProductVariation, Category, Product, Variation


def products_list(request):
    produtos = Product.objects.all().order_by('category__name', 'name')

    produtos_simples = produtos.filter(productvariation__isnull=True)

    variacoes = ProductVariation.objects.all()

    context = {
        'produtos_simples': produtos_simples,
        'variacoes': variacoes,
    }
    return render(request, 'products/list_products.html', context=context)


def product_new(request):
    product_form = Product()
    variations_formset = inlineformset_factory(Product, ProductVariation,
                                               form=ProductVariationForm,
                                               extra=1)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product_form, prefix='main')
        formset = variations_formset(request.POST, instance=product_form,
                                     prefix='product')

        if form.is_valid() and formset.is_valid():
            novo_produto = form.save(commit=False)
            novo_produto.save()
            formset.save()
            messages.success(request, "Novo produto cadastrado.")
            return redirect(products_list)
    else:
        form = ProductForm(instance=product_form, prefix='main')
        formset = variations_formset(instance=product_form, prefix='product')

    return render(request, 'products/product_new.html', {'form': form,
                                                         'formset': formset})


def two_flavors(request):
    variacoes = ProductVariation.objects.all()
    min_price_broto = ProductVariation.objects.filter(
        variation__name='Broto').aggregate(Min('price'))
    min_price_grande = ProductVariation.objects.filter(
        variation__name='Grande').aggregate(Min('price'))
    context = {
        'variacoes': variacoes,
        'min_price_broto': min_price_broto['price__min'],
        'min_price_grande': min_price_grande['price__min']
    }
    return render(request, 'products/sliced.html', context=context)


def categories_list(request):
    categories = Category.objects.all()
    context = {'categories': categories}

    return render(request, 'products/list_categories.html', context)


def category_new(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Nova categoria cadastrada.")
            return redirect(categories_list)
    else:
        form = CategoryForm()

    return render(request, 'products/category_new.html', {'form': form})


def variations_list(request):
    variacoes = Variation.objects.all()
    context = {'variacoes': variacoes}

    return render(request, 'products/list_variations.html', context)


def variation_new(request):
    if request.method == "POST":
        form = VariationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Nova variação cadastrada.")
            return redirect(variations_list)
    else:
        form = VariationForm()

    return render(request, 'products/variation_new.html', {'form': form})
