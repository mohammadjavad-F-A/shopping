from django.db import models
from datetime import datetime
class category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'images/')
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name

class product(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, blank=True)
    property_1 = models.CharField(max_length=20, blank=True)
    property_2 = models.CharField(max_length=20, blank=True)
    property_3 = models.CharField(max_length=20, blank=True)
    property_4 = models.CharField(max_length=20, blank=True)
    property_5 = models.CharField(max_length=20, blank=True)
    property_6 = models.CharField(max_length=20, blank=True)
    description = models.CharField(max_length=500, blank=True)

    price = models.IntegerField()
    old_price = models.IntegerField()
    star = models.IntegerField()

    mojod = models.BooleanField(default=True)
    is_published = models.BooleanField(default=False)
    is_old = models.BooleanField(default=False)

    image_main = models.ImageField(upload_to = 'images/')
    image_1 = models.ImageField(upload_to = 'images/')
    image_2 = models.ImageField(upload_to = 'images/')
    image_3 = models.ImageField(upload_to = 'images/')
    image_4 = models.ImageField(upload_to = 'images/')
    image_5 = models.ImageField(upload_to = 'images/')

    date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.name


