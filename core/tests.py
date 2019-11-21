from django.test import TestCase, Client, RequestFactory
from .views import index


# Create your tests here.
class DashboardViewTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.client = Client()

    def test_index_page_status_code_is_ok(self):
        request = self.factory.get('/')

        response = index(request)
        self.assertEqual(response.status_code, 200)
