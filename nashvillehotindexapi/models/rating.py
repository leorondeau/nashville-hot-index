from django.db import models

class Rating(models.Model):
    restaurantheat = models.ForeignKey("RestaurantHeat", on_delete=models.CASCADE)
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    rating = models.IntegerField(null=True, blank=True, default=None)