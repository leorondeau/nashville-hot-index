from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    website = models.CharField(max_length=250)
    img = models.ImageField(height_field=None, width_field=None, max_length=None)
    