from django.test import TestCase, Client, RequestFactory

from core.models import Company
from .views import index


# Create your tests here.
class IndexViewTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.client = Client()

        self.company = Company.objects.create(name='My Restaurant',
                                              address='FooBar street, with no number',
                                              phone='(11) 1234-5678',
                                              website='https://www.mulhergorila.com',
                                              facebook='https://www.mulhergorila.com',
                                              instagram='https://www.mulhergorila.com')

    def test_index_page_status_code_is_ok(self):
        request = self.factory.get('/')

        response = index(request)
        self.assertEqual(response.status_code, 200)

    def test_company_name_return_str(self):
        company = Company.objects.get(name=self.company.name)
        self.assertEqual(company.__str__(), self.company.name)
