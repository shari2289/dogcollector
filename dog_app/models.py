from django.db import models

# Create your models here.
class Dog(models.Model): 
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    characteristics = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name
        


    