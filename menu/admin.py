from django.contrib import admin
from .models import Menu, MenuCategory


# Register your models here.
class MenuCategoryInLine(admin.StackedInline):
    model = MenuCategory
    extra = 1


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [
        MenuCategoryInLine,
    ]


admin.site.register(Menu, MenuAdmin)
