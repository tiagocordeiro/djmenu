from django.forms import ModelForm, TextInput, Textarea, Select, NumberInput

from .models import Menu, MenuCategory


class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = [
            'name',
            'description',
        ]

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'})
        }


class MenuCategoriesForm(ModelForm):
    class Meta:
        model = MenuCategory
        fields = ['menu', 'category', 'order']

        widgets = {
            'category': Select(attrs={'class': 'form-control'}),
            'order': NumberInput(attrs={'class': 'form-control'}),
        }
