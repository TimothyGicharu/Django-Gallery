from django.db import models
from cloudinary import CloudinaryImage


class Image(models.Model):
    name = models.CharField(max_length =100)
    description = models.CharField(max_length=255)
    location = models.ForeignKey('Location',on_delete=models.CASCADE,)
    category = models.ForeignKey('Category',on_delete=models.CASCADE,)
    image = CloudinaryImage('image')

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update()

class Location(models.Model):
    name = models.CharField(max_length=30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location():
        pass

class Category(models.Model):
    category = models.CharField(max_length=30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category():
        pass