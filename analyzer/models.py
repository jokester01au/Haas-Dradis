from django.db import models


class HistoryRetrievalModel(models.Model):
    accountGuid = models.CharField(max_length=120)
    amountRetrieved = models.IntegerField(default=0)
    totalToRetrieve = models.IntegerField(default=0)
    started = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

class BasicAnalysisRunModel(models.Model):
    accountGuid = models.CharField(max_length=120)
    amountRetrieved = models.IntegerField(default=0)
    totalToRetrieve = models.IntegerField(default=0)
    started = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    botGuid = models.CharField(max_length=120)
    timeFrameInMinutes = models.IntegerField(default=0)
    isCustomBot = models.BooleanField(default=False)

class BasicAnalysisResultsModel(models.Model):
    accountGuid = models.CharField(max_length=120)
    exchangeName = models.CharField(max_length=120)
    baseBotGuid = models.CharField(max_length=120)
    baseBotName = models.CharField(max_length=120)
    primaryCurrency = models.CharField(max_length=120)
    secondaryCurrency = models.CharField(max_length=120)
    roi = models.CharField(max_length=120)
    isCustomBot = models.BooleanField(default=False)
