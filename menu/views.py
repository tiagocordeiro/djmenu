from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from qr_code.qrcode.utils import QRCodeOptions

from menu.models import Menu, MenuCategory
from .facade import menu_builder
from .forms import MenuForm, MenuCategoriesForm


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


def menu_qrcode_gen(request, pk):
    menu = Menu.objects.get(pk=pk)
    menu_url = reverse('menu-display', kwargs={'pk': pk})
    complete_url = ''.join(
        ['https://', get_current_site(request).domain, menu_url])
    qrcode_options = QRCodeOptions(size='M')

    context = {
        'menu': menu,
        'complete_url': complete_url,
        'qrcode_options': qrcode_options,
    }
    return render(request, 'menu/qr-gen.html', context=context)


def menu_qrcode_sheet_gen(request, pk, size):
    """
    Gera uma folha de QR codes.

    :param request:
    :param pk:
    :param size: passado para gerar o qrcode, pode ser:
    s - small
    m - medium (default)
    l - large
    ou um inteiro, exemplo: 50
    :return:
    """
    size = size
    menu = Menu.objects.get(pk=pk)
    menu_url = reverse('menu-display', kwargs={'pk': pk})
    complete_url = ''.join(
        ['https://', get_current_site(request).domain, menu_url])
    qrcode_options = QRCodeOptions(size=size)
    if size.lower() == 's':
        loop_time = range(0, 20)
    elif size.lower() == 'm':
        loop_time = range(0, 8)
    elif size.lower() == 'l':
        loop_time = range(0, 2)
    else:
        loop_time = range(0, 1)

    context = {
        'menu': menu,
        'menu_url': menu_url,
        'complete_url': complete_url,
        'qrcode_options': qrcode_options,
        'loop_time': loop_time,
    }
    return render(request, 'menu/qr-sheet-gen.html', context=context)


def menu_print(request, pk):
    menu = menu_builder(pk=pk)

    context = {
        'menu_title': menu['title'],
        'menu': menu['itens'],
    }

    return render(request, 'menu/food-menu-print.html', context=context)


def menu_json(request, pk):
    menu = menu_builder(pk=pk)

    context = {
        'menu_title': menu['title'],
        'menu': menu['itens'],
    }

    return JsonResponse(context)


def new_menu(request):
    menu_form = Menu()
    categories_menu_formset = inlineformset_factory(
        Menu, MenuCategory,
        form=MenuCategoriesForm, extra=1
    )
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu_form, prefix='main')
        formset = categories_menu_formset(request.POST,
                                          instance=menu_form,
                                          prefix='product')

        if form.is_valid() and formset.is_valid():
            novo_cardapio = form.save(commit=False)
            novo_cardapio.save()
            formset.save()
            messages.success(request, "Novo cardápio cadastrado.")
            return redirect('menu-list')

    else:
        form = MenuForm(instance=menu_form, prefix='main')
        formset = categories_menu_formset(instance=menu_form, prefix='product')

    return render(request, 'menu/create.html', {'form': form,
                                                'formset': formset})
