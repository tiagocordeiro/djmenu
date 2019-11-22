from django.test import TestCase, Client, RequestFactory
from .views import products_list, two_flavors
from .models import Product, Category, Variation, ProductVariation


# Create your tests here.
class ProductsViewTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.client = Client()

        # Category
        self.category_pizza = Category.objects.create(name='Pizzas')

        # Product
        self.margherita = Product.objects.create(name='Margherita',
                                                 category=self.category_pizza,
                                                 description='Molho de tomate, mussarela, folhas de manjericão...',
                                                 price=66)

        # Product Variations
        self.broto_variation = Variation.objects.create(name='Broto')
        self.grande_variation = Variation.objects.create(name='Grande')

        # Margherita variations
        self.margherita_broto = ProductVariation.objects.create(product=self.margherita,
                                                                variation=self.broto_variation,
                                                                price=42)
        self.margherita_grande = ProductVariation.objects.create(product=self.margherita,
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
