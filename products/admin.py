from django.contrib import admin

from .models import Product, Category, Ingredient, Variation, ProductVariation, ProductIngredient, ProductCategory


# Register your models here.
class ProductCategoryInLine(admin.StackedInline):
    model = ProductCategory
    extra = 1


class ProductIngredientInLine(admin.StackedInline):
    model = ProductIngredient
    extra = 1


class ProductVariationInLine(admin.StackedInline):
    model = ProductVariation
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)


class VariationAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [
        ProductCategoryInLine,
        ProductIngredientInLine,
        ProductVariationInLine,
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Variation, VariationAdmin)
