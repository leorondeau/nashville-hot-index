from django.db import models
from django.db.models.fields import BooleanField

class Order(models.Model):
    restaurant = models.ForeignKey("Restaurant", on_delete=models.CASCADE)
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    restaurantheat = models.ForeignKey("RestaurantHeat", on_delete=models.CASCADE)
    created_date = models.DateField(default="0000-00-00",)
    note = models.CharField(max_length=150, null=True)
    enjoyable = models.BooleanField(default=True, null=True)
