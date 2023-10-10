from django.test import Client, TestCase
from App.models import Register_table


class RegisterModelTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        
        
    def test_register_model(self):
        register = Register_table.objects.get(firstname='steve')
        self.assertEqual(register.firstname, 'test')
        self.assertEqual(register.lastname, 'test')
        self.assertEqual(register.email, 'mail@gmail.com')