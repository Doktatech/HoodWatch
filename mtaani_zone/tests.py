from django.test import TestCase
from .models import Business,Notices
import datetime as dt


# Create your tests here.
class BusinessTestClass(TestCase):
    def setUp(self):
        self.business= Business(name='McDonalds',address='17TH STREET',business_type='Fast_Foods',description='We offer fast foods')
    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))
    def test_save_method(self):
        self.business.save_business()
        business= Business.objects.all()
        self.assertTrue(len(business)>0)
    def tearDown(self):
        Business.objects.all().delete()
    def test_get_business(self):
        get_business = Business.get_business()
        self.assertTrue(len(get_business)>0)


class NoticesTestClass(TestCase):
    def setUp(self):
        self.notices= Notices(title='Nyumba Kumi',details='Monthly meeting',status='Urgent')
    def test_instance(self):
        self.assertTrue(isinstance(self.notices,Notices))
    def test_save_method(self):
        self.notices.save_notices()
        notices=Notices.objects.all()
        self.assertTrue(len(notices)>0)
    def tearDown(self):
        Notices.objects.all().delete()
    def test_get_notices(self):
        get_notices = Notices.get_notices()
        self.assertTrue(len(get_notices)>0)
