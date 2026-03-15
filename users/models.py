from django.db import models

# Create your models here.

class Users(models.Model):
    first_name = models.CharField(max_length=100)
    age = models.IntegerField()
    last_name = models.CharField(max_length=100)
    tel = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    def __str__(self):
        return self.first_name