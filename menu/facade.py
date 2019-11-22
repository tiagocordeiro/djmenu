import json
from .models import Menu
from products.models import Product, ProductVariation


def get_menu(pk):
    return Menu.objects.get(pk=pk)


def menu_builder(pk):
    menu = get_menu(pk=pk)

    menu_itens = []
    category_count = 0

    for category in menu.menucategory_set.select_related('category'):
        menu_itens.append({"category": category.category.name, "itens": []})
        product_count = 0

        for product in Product.objects.filter(category=category.category):
            if product.description:
                menu_itens[category_count]["itens"].append({"product": {"name": product.name,
                                                                        "description": product.description,
                                                                        "price": product.price}})
            else:
                menu_itens[category_count]["itens"].append({"product": {"name": product.name,
                                                                        "price": product.price}})

            variations = ProductVariation.objects.filter(product=product)
            if variations:
                menu_itens[category_count]["itens"][product_count]["product"]["price"] = []

                for variation in variations:
                    variacao = ProductVariation.objects.get(pk=variation.pk)
                    menu_itens[category_count]["itens"][product_count]["product"]["price"].append(
                        {
                            "variation_name": variacao.variation.name,
                            "variation_price": variation.price
                        })

            product_count += 1
        category_count += 1

    return menu_itens
