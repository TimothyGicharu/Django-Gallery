from django.db import models
from cloudinary.models import CloudinaryField


class Image(models.Model):
    name = models.CharField(max_length =100)
    description = models.CharField(max_length=255)
    location = models.ForeignKey('Location',on_delete=models.CASCADE,)
    category = models.ForeignKey('Category',on_delete=models.CASCADE,)
    image = CloudinaryField('image')

    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update()

    @classmethod
    def search_by_category(cls, search_word):
        images = cls.objects.filter(category__name__icontains=search_word)
        return images

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural= 'Images'

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location():
        pass

    def __str__(self):
        return self.name

class Category(models.Model):
    category = models.CharField(max_length=30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category():
        pass

    def __str__(self):
        return self.category