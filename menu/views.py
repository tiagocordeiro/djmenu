from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from qr_code.qrcode.utils import QRCodeOptions

from menu.models import Menu
from .facade import menu_builder, render_to_pdf


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
    complete_url = ''.join(['https://', get_current_site(request).domain, menu_url])
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
    complete_url = ''.join(['https://', get_current_site(request).domain, menu_url])
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


def menu_pdf_gen(request, pk):
    menu = menu_builder(pk=pk)

    context = {
        'menu_title': menu['title'],
        'menu': menu['itens'],
    }

    pdf = render_to_pdf('menu/food-menu-pdf.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = f"Menu-{menu['title']}.pdf"
        content = f"inline; filename={filename}"
        download = request.GET.get("download")
        if download:
            content = f"attachment; filename='{filename}'"
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")


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
