from django.shortcuts import render
from .models import Menu


# Create your views here.
def menu_display(request, pk):
    menu = Menu.objects.get(pk=pk)

    context = {
        'menu': menu,
    }

    return render(request, 'menu/food-menu.html', context=context)
