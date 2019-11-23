from django.test import TestCase, RequestFactory, Client

from products.models import Product, Category, ProductVariation, Variation
from .facade import menu_builder
from .models import Menu, MenuCategory
from .views import menu_display


# Create your tests here.
class MenuViewTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.client = Client()

        # Product categories example
        self.rotolinas = Category.objects.create(name='Rotolinas')
        self.petiscos = Category.objects.create(name='Petiscos')
        self.doces = Category.objects.create(name='doces')

        # Simple product
        self.spaghetti = Product.objects.create(name='Rotolinas Funghi',
                                                category=self.rotolinas,
                                                description='Provolone, shitake, champignon, parmesão e manjericão.',
                                                price=48)

        # Product without description
        self.brigadeiro = Product.objects.create(name='Brigadeiro',
                                                 category=self.doces,
                                                 price=4.5)

        # Variable product
        self.bandeijao = Product.objects.create(name='Bandeijão',
                                                category=self.petiscos,
                                                description='Porção de petiscos variados. Serve até 4 pessoas.',
                                                price=33)

        # Product variations
        self.porcao_meia = Variation.objects.create(name='Meia')
        self.porcao_inteira = Variation.objects.create(name='Inteira')

        # Petiscos variations
        self.petiscos_meia = ProductVariation.objects.create(product=self.bandeijao,
                                                             variation=self.porcao_meia,
                                                             price=22)
        self.petiscos_inteira = ProductVariation.objects.create(product=self.bandeijao,
                                                                variation=self.porcao_inteira,
                                                                price=33)

        # Create Menu
        self.menu_almoco = Menu.objects.create(name='Almoço')

        # Select categories to menu
        self.menu_category = MenuCategory.objects.create(menu=self.menu_almoco, category=self.rotolinas, order=1)
        self.menu_category = MenuCategory.objects.create(menu=self.menu_almoco, category=self.petiscos, order=2)
        self.menu_category = MenuCategory.objects.create(menu=self.menu_almoco, category=self.doces, order=3)

    def test_manu_page_status_code_is_ok(self):
        request = self.factory.get(f'/menu/view/{self.menu_almoco.pk}/')

        response = menu_display(request, pk=self.menu_almoco.pk)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Almoço')

    def test_menu_builder_return(self):
        self.menu = menu_builder(pk=self.menu_almoco.pk)
        print()

        self.assertEqual(self.menu['title'], self.menu_almoco.name)
