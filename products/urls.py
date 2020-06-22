from django.urls import path

from . import views

urlpatterns = [
    path('new/', views.product_new, name='product_new'),
    path('list/', views.products_list, name='products-list'),
    path('list/two-flavors/', views.two_flavors, name='two-flavors'),
    path('categories/', views.categories_list, name="categories_list"),
    path('category/new/', views.category_new, name="category_new"),
    path('variations/', views.variations_list, name="variations_list"),
    path('variation/new/', views.variation_new, name="variation_new"),
    path('import/woo/<product_id>/',
         views.import_from_woocommerce,
         name="import_from_woocommerce"),
    path('import/woo/category/<category_id>/',
         views.import_all_from_woocommerce_category,
         name="import_all_from_woocommerce_category"),
]
