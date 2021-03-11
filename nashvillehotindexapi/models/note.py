from django.db import models

class Note(models.Model):
    restaurant = models.ForeignKey("Restaurant", on_delete=models.CASCADE)
    eater = models.ForeignKey("Eater", on_delete=models.CASCADE)
    note = models.CharField(max_length=250)