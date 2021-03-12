from django.db import models
from django.db.models.fields import BooleanField

class Order(models.Model):
    restaurant = models.ForeignKey("Restaurant", on_delete=models.CASCADE)
    customer = models.ForeignKey("Eater", on_delete=models.CASCADE)
    restaurantheat = models.ForeignKey("Heat", on_delete=models.CASCADE)
    note = models.CharField(max_length=150, null=True)
    enjoyable = models.BooleanField(default=True, null=True)
