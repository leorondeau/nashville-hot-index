from django.db import models
from django.db.models.fields import BooleanField

class Order(models.Model):
    restaurant = models.ForeignKey("Restaurant", on_delete=models.CASCADE)
    eater = models.ForeignKey("Eater", on_delete=models.CASCADE)
    heat = models.ForeignKey("Heat", on_delete=models.CASCADE)
    reaction = models.CharField(max_length=150, null=True)
    enjoyable = models.BooleanField(default=True, null=True)

