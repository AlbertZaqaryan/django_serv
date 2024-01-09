from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField('Category name', max_length=60)

    def __str__(self):
        return self.name
    
class CarModel(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='car_categ')
    name = models.CharField('CarModel name', max_length=60)
    price = models.PositiveIntegerField('CarModel price')
    img = models.ImageField('CarModel image', upload_to='images')

    def __str__(self):
        return self.name