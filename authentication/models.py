from django.db import models

class ConfigurationModel(models.Model):
    haasIp = models.CharField(max_length=120)
    haasPort = models.IntegerField()
    haasSecret = models.CharField(max_length=120)

    numConcurrentTest = models.IntegerField()