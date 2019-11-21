from django.shortcuts import render
from .models import Menu

from products.models import ProductCategory, Category


# Create your views here.
def menu_display(request, pk):
    # menu = get_object_or_404(Menu, pk=pk)
    menu = Menu.objects.get(pk=pk).menucategory_set.values()

    categories_menu = []
    products_menu = []

    for category in menu:
        category_name = Category.objects.get(pk=category['category_id']).name
        category_products = ProductCategory.objects.filter(category__pk=category['category_id'])

        products = []

        for product in category_products:
            products.append(product.product.name)

        categories_menu.append(f"{category_name}: {products}")

        print(category_name)
        print(category_products)

    context = {
        'menu': menu,
        'categories_menu': categories_menu,
        'products_menu': products_menu,
    }

    return render(request, 'menu/food-menu.html', context=context)
