from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.products_list, name='products-list'),
    path('list/two-flavors', views.two_flavors, name='two-flavors'),
]
