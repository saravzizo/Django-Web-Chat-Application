from django.test import TestCase
from App.models import Register_table


class RegisterModelTestCase(TestCase):
    def setUp(self):
        Register_table.objects.create(firstname='test', lastname='test',
                                      email = 'mail@gmail.com', password='test')
        
    def test_register_model(self):
        register = Register_table.objects.get(firstname='test')
        self.assertEqual(register.firstname, 'test')
        self.assertEqual(register.lastname, 'test')
        self.assertEqual(register.email, 'mail@gmail.com')