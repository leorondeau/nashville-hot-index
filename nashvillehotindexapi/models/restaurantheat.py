from django.db import models

class RestaurantHeat(models.Model):
    restaurant = models.ForeignKey("Restaurant", on_delete=models.CASCADE)
    name = models.ForeignKey("Heat", on_delete=models.CASCADE)