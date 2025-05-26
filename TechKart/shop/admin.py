# Register your models here.
from django.contrib import admin
from .models import Product
#Here we can register projects to the admin site
admin.site.register(Product)
