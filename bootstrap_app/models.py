from django.db import models

# Create your models here.


class Trail(models.Model):
    name = models.CharField(max_length=30)
    one_way_length = models.FloatField()
    hours_hiking_time = models.FloatField()
    trailhead = models.CharField(max_length=30)
    image_link = models.CharField(max_length=100)
    blurb = models.CharField(max_length=500)

    def __str__(self):
        return "{} Trail".format(self.name)