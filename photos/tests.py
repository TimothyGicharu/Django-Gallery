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

    def test_get_image_by_id(self):
        pass

    def tearDown(self):
        Image.objects.all().delete()



class TestLocation(TestCase):
    def setUp(self):
        self.new_location = Location(name='Nairobi')

    def test_category_instance(self):
        self.assertTrue(isinstance(self.new_location, Location))

    def save_location(self):
        before = Location.objects.count()
        self.new_location.save_location()
        after = Location.objects.count()
        self.assertTrue(before < after)

    def tearDown(self):
        Location.objects.all().delete()


class TestCategory(TestCase):
    def setUp(self):
        self.new_category = Category(category='cars')

    def test_category_instance(self):
        pass

    def test_save_category(self):
        before = Category.objects.count()
        self.new_category.save_category()
        after = Category.objects.count()
        self.assertTrue(before < after)

    def test_delete_category(self):
        before = Category.objects.count()
        self.new_category.delete_category()
        after = Category.objects.count()
        self.assertTrue(before > after)

    def tearDown(self):
        Category.objects.all().delete()