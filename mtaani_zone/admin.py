from django.contrib import admin
from .models import Notices, Business,Profile

# Register your models here.
admin.site.register(Business)
admin.site.register(Notices)
admin.site.register(Profile)