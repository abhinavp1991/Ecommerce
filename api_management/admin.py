from django.contrib import admin
from api_management import models
from salesforce.testrunner.example.universal_admin import register_omitted_classes
# Register your models here.

admin.site.register(models.Product)
