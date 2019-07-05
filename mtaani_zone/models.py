from django.db import models

# Create your models here.
class Business(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    business_type=models.CharField(max_length=30)
    description=models.TextField()
    def __str__(self):
        return self.name
    def save_business(self):
        self.save()
class Notices(models.Model):
    Status_Choices=(
        (1,'Urgent'),
        (2,'Necessary'),
        (3,'Unessential'),
    )
    title=models.CharField(max_length=50)
    details=models.TextField()
    status= models.CharField(max_length=50, choices=Status_Choices,default='1')
    def __str__(self):
        return self.title
    def save_notices(self):
        self.save()