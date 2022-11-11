from django.db import models
from datetime import date

class Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category
    
class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.FloatField()
    description = models.TextField()
    data_upload = models.DateTimeField(date.today(), blank=True)
    image = models.ImageField(upload_to='products/', blank=True)

    def __str__(self):
        return self.name
