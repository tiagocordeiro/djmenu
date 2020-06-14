from menu.models import Menu
from products.models import Product, Category


def get_dashboard_data_summary():
    cardapios = Menu.objects.all()
    produtos = Product.objects.all()
    categorias = Category.objects.all()

    return {'total_cardapios': len(cardapios),
            'total_produtos': len(produtos),
            'total_categorias': len(categorias)}
