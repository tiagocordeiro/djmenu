from django.test import TestCase, RequestFactory, Client

from products.models import Product, Category, ProductVariation, Variation
from .facade import menu_builder
from .models import Menu, MenuCategory
from .views import menu_display, menu_list, menu_qrcode_gen, menu_qrcode_sheet_gen, menu_json


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

    def test_menu_page_status_code_is_ok(self):
        request = self.factory.get(f'/menu/view/{self.menu_almoco.pk}/')

        response = menu_display(request, pk=self.menu_almoco.pk)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Almoço')

    def test_menu_builder_return(self):
        self.menu = menu_builder(pk=self.menu_almoco.pk)

        self.assertEqual(self.menu['title'], self.menu_almoco.name)

    def test_menu_list_status_code_is_ok(self):
        request = self.factory.get('/menu/list/')

        response = menu_list(request)
        self.assertEqual(response.status_code, 200)

    def test_qrcode_gen_status_code(self):
        request = self.factory.get(f'/menu/qrcode/{self.menu_almoco.pk}')

        response = menu_qrcode_gen(request, pk=self.menu_almoco.pk)
        self.assertEqual(response.status_code, 200)

    def test_qrcode_gen_sheet_status_code(self):
        request_large = self.factory.get(f'/menu/sheet/{self.menu_almoco.pk}/l')
        request_medio = self.factory.get(f'/menu/sheet/{self.menu_almoco.pk}/m')
        request_small = self.factory.get(f'/menu/sheet/{self.menu_almoco.pk}/s')
        request_with_number = self.factory.get(f'/menu/sheet/{self.menu_almoco.pk}/45')

        response_large = menu_qrcode_sheet_gen(request_large, pk=self.menu_almoco.pk, size='l')
        response_medio = menu_qrcode_sheet_gen(request_medio, pk=self.menu_almoco.pk, size='m')
        response_small = menu_qrcode_sheet_gen(request_small, pk=self.menu_almoco.pk, size='s')
        response_with_number = menu_qrcode_sheet_gen(request_with_number, pk=self.menu_almoco.pk, size='45')
        self.assertEqual(response_large.status_code, 200)
        self.assertEqual(response_medio.status_code, 200)
        self.assertEqual(response_small.status_code, 200)
        self.assertEqual(response_with_number.status_code, 200)

    def test_json_return(self):
        request = self.factory.get(f'/menu/json/{self.menu_almoco.pk}')

        response = menu_json(request, pk=self.menu_almoco.pk)
        self.assertEqual(response.status_code, 200)
