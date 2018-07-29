from django.db import models

# Create your models here.
from django.db import models

class HistoryRetrievalModel(models.Model):
    accountGuid = models.CharField(max_length=120)
    amountRetrieved = models.IntegerField()
    totalToRetrieve = models.IntegerField()
    started = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)