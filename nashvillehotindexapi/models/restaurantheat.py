from django.db import models

class RestaurantHeat(models.Model):
    restaurant = models.ForeignKey("Restaurant", on_delete=models.CASCADE, related_name="heatlevels")
    name = models.CharField(max_length=50)