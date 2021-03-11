from django.db import models

class Rating(models.Model):
    heat = models.ForeignKey("Heat", on_delete=models.CASCADE)
    eater = models.ForeignKey("Eater", on_delete=models.CASCADE)
    rating = models.IntegerField(null=True, blank=True, default=None)