from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
class Business(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    business_type=models.CharField(max_length=30)
    description=models.TextField()
    business_image = models.ImageField(upload_to = 'photos/')
    def __str__(self):
        return self.name
    def save_business(self):
        self.save()
    @classmethod
    def get_business(cls):
        business=cls.objects.all()
        return business
    @classmethod
    def search_by_type(cls,search_term):
        business = cls.objects.filter(business_type__icontains=search_term)
        return business

class Notices(models.Model):
    Status_Choices=(
        ('1','Urgent'),
        ('2','Necessary'),
        ('3','Unessential'),
    )
    title=models.CharField(max_length=50)
    details=models.TextField()
    status= models.CharField(max_length=50, choices=Status_Choices,default='None')
    pub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    def save_notices(self):
        self.save()
    class Meta:
        ordering =['status']
    @classmethod
    def get_notices(cls):
        today = dt.date.today()
        notices=cls.objects.filter(pub_date__date=today)
        return notices
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to='profile/')
    
    def __str__(self):
        return self.first_name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profiles(cls):
        profiles = cls.objects.all()
        return profiles
    
    @classmethod
    def search_by_username(cls,search_term):
        profiles = cls.objects.filter(title__icontains=search_term)
        return profiles
