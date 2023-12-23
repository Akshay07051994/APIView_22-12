from django.db import models

# Create your models here.


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=200)
    product_category = models.CharField(max_length=200)
    product_type = models.CharField(max_length=200)
    product_mfg = models.DateTimeField()
    product_sku = models.IntegerField()
    
