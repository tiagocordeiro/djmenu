from django.test import TestCase, Client, RequestFactory
from django.urls import reverse

from .admin import CompanyAdmin
from .models import Company
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

    def test_company_admin_add_company_return_false(self):
        request = reverse('admin:core_company_changelist')
        has_add_permission = CompanyAdmin.has_add_permission(self.company, request)
        self.assertEqual(has_add_permission, False)

    def test_returns_true_when_no_business_data_exists(self):
        self.company.delete()

        request = reverse('admin:core_company_changelist')
        has_add_permission = CompanyAdmin.has_add_permission(self.company, request)
        self.assertEqual(has_add_permission, True)
