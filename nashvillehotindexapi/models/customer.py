from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    heat_tolerance = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)],)