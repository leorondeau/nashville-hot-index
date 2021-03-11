from django.db import models
from django.contrib.auth.models import User

class Eater(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50)
    heat_tolerance = models.IntegerField(null=True, blank=True, default=None)