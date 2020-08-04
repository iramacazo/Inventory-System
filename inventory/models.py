from django.db import models


# Create your models here.

class Product(models.Model):
    id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2)
    quantity = models.IntegerField(default=0)


class ProductMovement(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField
    movement_type = models.CharField(max_length=3, choices=['In', 'Out'])
    quantity = models.IntegerField()
