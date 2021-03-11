from typing import ChainMap
from django.db import models
from django.db.models.fields import CharField

class Heat(models.Model):
    name = models.CharField(max_length=50)