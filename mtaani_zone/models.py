from django.db import models
import datetime as dt

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
    