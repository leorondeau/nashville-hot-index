from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    website = models.CharField(max_length=250)
    img = models.ImageField()

    @property
    def suggested_heat(self):
        return self.__suggested_heat

    @suggested_heat.setter
    def suggested_heat(self, value):
        self.__suggested_heat = value