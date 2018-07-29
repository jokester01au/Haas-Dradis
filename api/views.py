import logging
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from analyzer.models import HistoryRetrievalModel

from managers.HistoryRetrievalManager import HistoryRetrievalManager

@login_required
def get_history_retrieval_status_api(request):
    
    context = {}

    historyStatus = HistoryRetrievalManager.get_or_create_history_retrieval_model()


    context['amountRetrieved'] = historyStatus.amountRetrieved
    context['totalToRetrieve'] = historyStatus.totalToRetrieve
    context['percentageToShow'] = historyStatus.amountRetrieved/historyStatus.totalToRetrieve*100

    return JsonResponse(context)