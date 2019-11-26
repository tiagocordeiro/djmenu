from django.urls import path

from . import views

urlpatterns = [
    path('view/<pk>/', views.menu_display, name='menu-display'),
    path('json/<pk>/', views.menu_json, name='menu-json'),
    path('list/', views.menu_list, name='menu-list'),
    path('qrcode/<pk>', views.menu_qrcode_gen, name='qr-gen'),
    path('qrcode/sheet/<pk>/<size>', views.menu_qrcode_sheet_gen, name='qr-sheet-gen'),
    path('print/<pk>', views.menu_print, name='menu-print'),
]
