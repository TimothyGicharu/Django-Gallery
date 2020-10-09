from django.db import models

class Image(models.Model):
    name = models.CharField(max_length =30)
    description = models.CharField(max_length=255)
    location = models.ForeignKey('Location',on_delete=models.CASCADE,)
    category = models.ForeignKey('Category',on_delete=models.CASCADE,)



class Location(models.Model):
    name = models.CharField(max_length=30)

class Category(models.Model):
    category = models.CharField(max_length=30)
