
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

class RegisterViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('register')

    def test_register_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')
        self.assertContains(response, 'Register Page') 

class LoginViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('login')

    def test_login_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertContains(response, 'Login Page')


        

 