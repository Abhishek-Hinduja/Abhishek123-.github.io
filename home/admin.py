from django.contrib import admin
from django.contrib.admin.decorators import register
from home.models import Contact

# Register your models here.
admin.site.register(Contact)
