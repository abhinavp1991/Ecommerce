from django.db import models
from salesforce.models import SalesforceModel
# Create your models here.

class Product(SalesforceModel):
    Name = models.CharField(max_length=255)
    Price = models.IntegerField(null=False)
