from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Rating(models.Model):
    restaurantheat = models.ForeignKey("RestaurantHeat", on_delete=models.CASCADE, related_name="ratings")
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)],)
