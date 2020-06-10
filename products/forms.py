from django.forms import ModelForm, TextInput, Textarea, NumberInput, Select

from .models import Product, Category, Variation, ProductVariation


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',
            'description',
        ]

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'})
        }


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'category',
        ]

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'price': NumberInput(attrs={'class': 'form-control'}),
            'category': Select(attrs={'class': 'form-control'}),
        }


class VariationForm(ModelForm):
    class Meta:
        model = Variation
        fields = [
            'name',
            'description',
        ]

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'})
        }


class ProductVariationForm(ModelForm):
    class Meta:
        model = ProductVariation
        fields = [
            'product',
            'variation',
            'price',
        ]

        widgets = {
            'product': Select(attrs={'class': 'form-control'}),
            'variation': Select(attrs={'class': 'form-control'}),
            'price': NumberInput(attrs={'class': 'form-control'}),
        }
