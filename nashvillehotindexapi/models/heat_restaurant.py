from django.db import models

class HeatRestaurant(models.Model):
    restaurant = models.ForeignKey("Restaurant", on_delete=models.CASCADE)
    heat = models.ForeignKey("Heat", on_delete=models.CASCADE)