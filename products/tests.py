from django.contrib.messages.storage.fallback import FallbackStorage
from django.forms import inlineformset_factory
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse

from .forms import CategoryForm, ProductForm, VariationForm, \
    ProductVariationForm
from .views import products_list, two_flavors, categories_list, category_new, \
    product_new, variations_list, variation_new
from .models import Product, Category, Variation, ProductVariation


# Create your tests here.
class ProductsViewTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.client = Client()

        # Category
        self.category_pizza = Category.objects.create(name='Pizzas')
        self.category_sucos = Category.objects.create(name='Suco natural')

        # Product
        description = 'Molho de tomate, mussarela, folhas de manjericão...'
        self.margherita = Product.objects.create(name='Margherita',
                                                 category=self.category_pizza,
                                                 description=description,
                                                 price=66)

        # Product Variations
        self.broto_variation = Variation.objects.create(name='Broto')
        self.grande_variation = Variation.objects.create(name='Grande')

        # Margherita variations
        self.margherita_broto = ProductVariation.objects.create(
            product=self.margherita,
            variation=self.broto_variation,
            price=42)
        self.margherita_grande = ProductVariation.objects.create(
            product=self.margherita,
            variation=self.grande_variation,
            price=66)

    def test_products_list_page_status_code_is_ok(self):
        request = self.factory.get('/products/list/')

        response = products_list(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Margherita')

    def test_product_with_two_flavors(self):
        request = self.factory.get('/products/list/two-flavors')

        response = two_flavors(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '42,00')

    def test_product_name_str_return(self):
        product = Product.objects.get(pk=self.margherita.pk)

        self.assertEqual(product.name, 'Margherita')

    def test_category_name_return(self):
        category = Category.objects.get(pk=self.category_pizza.pk)

        self.assertEqual(category.__str__(), 'Pizzas')

    def test_product_variation_name_return(self):
        expected = 'Margherita - Broto - 42'
        self.assertEqual(self.margherita_broto.__str__(), expected)

    def test_categories_list_status_code_is_ok(self):
        request = self.client.get(reverse('categories_list'))

        response = categories_list(request)
        self.assertEqual(response.status_code, 200)

    def test_category_new_view_status_code_is_ok(self):
        request = self.client.get(reverse('category_new'))
        self.assertEqual(request.status_code, 200)

    def test_category_crete_new(self):
        categories = Category.objects.all()
        self.assertEqual(len(categories), 2)
        self.assertEqual(Category.objects.count(), 2)

        new_category = {
            'name': 'Nova Categoria',
            'description': 'Categoria de testes',
        }

        form = CategoryForm(new_category)
        self.assertEqual(form.is_valid(), True)

        request = self.factory.post(reverse('category_new'), data=new_category)
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)

        response = category_new(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/products/categories/')

        categories = Category.objects.all()
        self.assertEqual(len(categories), 3)
        self.assertEqual(Category.objects.count(), 3)

    def test_product_new_view_status_code_is_ok(self):
        request = self.client.get(reverse('product_new'))
        self.assertEqual(request.status_code, 200)

    def test_product_crete_new(self):
        products = Product.objects.all()
        self.assertEqual(len(products), 1)
        self.assertEqual(Product.objects.count(), 1)

        new_product = {
            'main-name': 'Novo produto',
            'main-description': 'Produto simples de testes',
            'main-price': 5.20,
            'main-category': self.category_sucos.pk,
            'product-TOTAL_FORMS': 2,
            'product-INITIAL_FORMS': 0,
            'product-MIN_NUM_FORMS': 0,
            'product-MAX_NUM_FORMS': 1000,
            'product-0-variation': self.broto_variation.pk,
            'product-0-price': 10,
            'product-1-variation': self.grande_variation.pk,
            'product-1-price': 20,
        }

        product_form = Product()
        variations_formset = inlineformset_factory(Product, ProductVariation,
                                                   form=ProductVariationForm,
                                                   extra=1)

        form = ProductForm(new_product, instance=product_form, prefix='main')
        formset = variations_formset(new_product, instance=product_form,
                                     prefix='product')

        request = self.factory.post(reverse('product_new'), data=new_product)
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)

        self.assertEqual(form.is_valid(), True)
        self.assertEqual(formset.is_valid(), True)

        response = product_new(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/products/list/')

        products = Product.objects.all()
        self.assertEqual(len(products), 2)
        self.assertEqual(Product.objects.count(), 2)

    def test_variations_list_status_code_is_ok(self):
        request = self.client.get(reverse('variations_list'))

        response = variations_list(request)
        self.assertEqual(response.status_code, 200)

    def test_variation_new_view_status_code_is_ok(self):
        request = self.client.get(reverse('variation_new'))
        self.assertEqual(request.status_code, 200)

    def test_variation_crete_new(self):
        variations = Variation.objects.all()
        self.assertEqual(len(variations), 2)
        self.assertEqual(Variation.objects.count(), 2)

        form_data = {
            'name': 'Quilo',
            'description': 'Valor por quilo',
        }

        form = VariationForm(form_data)
        self.assertEqual(form.is_valid(), True)

        request = self.factory.post(reverse('variation_new'), data=form_data)
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)

        response = variation_new(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/products/variations/')

        variations = Variation.objects.all()
        self.assertEqual(len(variations), 3)
        self.assertEqual(Variation.objects.count(), 3)
