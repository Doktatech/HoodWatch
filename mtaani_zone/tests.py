from django.test import TestCase
from .models import Business


# Create your tests here.
class BusinessTest(TestCase):
    def setUp(self):
        self.business=Business(name='McDonalds',address='17TH STREET',business_type='Fast_Foods',description='We offer fast foods')
    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))