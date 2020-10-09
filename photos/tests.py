from django.test import TestCase
from .models import Image, Location, Category


class TestImage(TestCase):
    def setUp(self):
        self.location = Location(name='Nakuru')
        self.location.save_location()

        self.category = Category(category='Nature')
        self.category.save_category()

        self.image = Image(name='Monalisa', description='Monalisa potrait painted by DaVinci',
                           location=self.location, category=self.category)
        self.image.save_image()


    def test_save_image(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_update_image(self):
        pass

    def test_get_image_by_id(self)