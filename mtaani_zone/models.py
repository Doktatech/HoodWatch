from django.db import models
import datetime as dt
from django.contrib.auth.models import User
# from django.core.validators import email_re

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to='profile/')
    neighborhood = models.ForeignKey('Neighborhood', blank=True, null=True)
    
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
class Neighborhood(models.Model):
    neigborhood_name=models.CharField(max_length=70,blank=False,null=True)
    neigborhood_location=models.CharField(max_length=70,blank=False,null=True)
    occupants_count=models.IntegerField(blank=False, null= False)
    admin = models.ForeignKey(Profile, related_name='hoods', null=True)
    image = models.ImageField(upload_to='neighborimage/', null=True)


class Business(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    business_type=models.CharField(max_length=30)
    description=models.TextField()
    business_image = models.ImageField(upload_to = 'photos/')
    neighborhood = models.ForeignKey(Neighborhood, related_name='businesses')
    profile = models.ForeignKey(Profile, related_name='profiles')
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)

    def __str__(self):
        return self.name
    # def save(self, *args, **kwargs):
    # # ... other things not important here
    #     self.email = self.email.lower().strip() # Hopefully reduces junk to ""
    #     if self.email != "": # If it's not blank
    #         if not email_re.match(self.email): # If it's not an email address
    #             raise ValidationError(u'%s is not an email address, dummy!' % self.email)
    #     if self.email == "":
    #         self.email = None
    #     super(Business, self).save(*args, **kwargs)
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
    user = models.ForeignKey(Profile, related_name='profile')
    title=models.CharField(max_length=50)
    details=models.TextField()
    status= models.CharField(max_length=50, choices=Status_Choices,default='None')
    pub_date = models.DateTimeField(auto_now_add=True)
    neighborhood = models.ForeignKey(Neighborhood, related_name='posts')
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
