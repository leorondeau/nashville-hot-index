from django.db import models


class Heat(models.Model):
    name = models.CharField(max_length=50)