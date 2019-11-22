from django.test import TestCase, RequestFactory, Client

from .models import Menu

from .views import menu_display


# Create your tests here.
class MenuViewTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.client = Client()

        self.menu_almoco = Menu.objects.create(name='Almoço')

    def test_manu_page_status_code_is_ok(self):
        request = self.factory.get(f'/menu/view/{self.menu_almoco.pk}/')

        response = menu_display(request, pk=self.menu_almoco.pk)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Almoço')
