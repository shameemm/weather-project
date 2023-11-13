from django.contrib.gis.db import models

class Location(models.Model):
    location = models.PointField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
