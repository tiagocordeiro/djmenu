from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django.urls import reverse
from qr_code.qrcode.utils import ContactDetail as QRCodeDetails, QRCodeOptions

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


def menu_qrcode_gen(request, pk):
    menu = Menu.objects.get(pk=pk)
    menu_url = reverse('menu-display', kwargs={'pk': pk})
    qrcode_details = QRCodeDetails(
        url=''.join(['https://', get_current_site(request).domain, menu_url])
    )
    qrcode_options = QRCodeOptions(size='M')

    context = {
        'menu': menu,
        'menu_url': menu_url,
        'qrcode_options': qrcode_options,
        'qrcode_details': qrcode_details,
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
    qrcode_details = QRCodeDetails(
        url=''.join(['https://', get_current_site(request).domain, menu_url])
    )
    qrcode_options = QRCodeOptions(size=size)
    if size.lower() == 's':
        loop_time = range(0, 30)
    elif size.lower() == 'm':
        loop_time = range(0, 15)
    elif size.lower() == 'l':
        loop_time = range(0, 6)
    else:
        loop_time = range(0, 1)

    context = {
        'menu': menu,
        'menu_url': menu_url,
        'qrcode_options': qrcode_options,
        'qrcode_details': qrcode_details,
        'loop_time': loop_time,
    }
    return render(request, 'menu/qr-sheet-gen.html', context=context)
