from django.db import models

class Sensor(models.Model):
    pabrik = models.IntegerField()
    subsistem = models.IntegerField()
    name = models.CharField(max_length=100)
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
