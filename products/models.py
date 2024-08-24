from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.title)
    