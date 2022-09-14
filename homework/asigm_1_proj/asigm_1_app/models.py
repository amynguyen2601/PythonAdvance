from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.SmallIntegerField(default=0)
    address = models.CharField(max_length=500)
    mobile_number = models.IntegerField(default=0)
    def __str__(self):
        return self.name