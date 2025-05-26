# Register your models here.

from django.contrib import admin
from .models import Product
#Here we can register projects
admin.site.register(Product)
