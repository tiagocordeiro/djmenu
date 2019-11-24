from django.shortcuts import render

from menu.models import Menu
from .facade import menu_builder


# Create your views here.
def menu_display(request, pk):
    menu = menu_builder(pk=pk)

    context = {
        'menu_title': menu['title'],
        'menu': menu['itens'],
    }

    return render(request, 'menu/food-menu.html', context=context)


def menu_list(request):
    menus = Menu.objects.all()

    return render(request, 'menu/list.html', context={'menus': menus})
