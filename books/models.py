from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    author = models.CharField(max_length=25, blank=True, null=True)
    isbn = models.CharField(max_length=13, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    genre = models.CharField(max_length=25, blank=True, null=True)
    def __str__(self):
        return self.title
