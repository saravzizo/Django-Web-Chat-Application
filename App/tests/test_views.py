
from django.test import TestCase, Client
from django.urls import reverse
from App.models import Register_table
from App.views import Register


class HomeViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('Home')

    def test_home_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'Hi There Welcome Home')


 