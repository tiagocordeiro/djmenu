from django.urls import path

from . import views

urlpatterns = [
    path('view/<pk>/', views.menu_display, name='menu-display'),
]
