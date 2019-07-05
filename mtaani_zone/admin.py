from django.contrib import admin
from .models import Notices, Business

# Register your models here.
admin.site.register(Business)
admin.site.register(Notices)