from django.core.validators import ip_address_validator_map
from django.contrib.auth.models import User
from django.db import models
from .rating import Rating


class RestaurantHeat(models.Model):
    restaurant = models.ForeignKey("Restaurant", on_delete=models.CASCADE, related_name="heatlevels")
    name = models.CharField(max_length=50)

    @property
    def average_rating(self):
        """Average rating calculated attribute for each heat level
        by restaurant
        Returns:
            number -- The average rating for the each
        """
        ratings = Rating.objects.filter(restaurantheat=self)
        total_rating = 0
        for rating in ratings:
            total_rating += rating.rating
        try:
            avg = total_rating / len(ratings)
            limited_float = round(avg, 1)
        except ZeroDivisionError:
            return 0
        return limited_float

   



    
