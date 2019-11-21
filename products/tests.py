from django.test import TestCase, Client, RequestFactory
from .views import products_list
from .models import Product, Category, Variation, ProductVariation, ProductCategory


# Create your tests here.
class DashboardViewTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.client = Client()

        # Product
        self.margherita = Product.objects.create(name='Margherita',
                                                 description='Molho de tomate, mussarela, folhas de manjericão...',
                                                 price=66)

        # Category
        self.category_pizza = Category.objects.create(name='Pizzas')

        # Margherita Category
        self.margherita_category = ProductCategory.objects.create(product=self.margherita, category=self.category_pizza)

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
