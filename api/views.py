import logging
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from analyzer.models import HistoryRetrievalModel
from analyzer.models import BasicAnalysisResultsModel

from managers.BasicAnalysisManager import BasicAnalysisManager
from managers.HistoryRetrievalManager import HistoryRetrievalManager


@login_required
def get_history_retrieval_status_api(request):
    
    context = {}

    historyStatus = HistoryRetrievalManager.get_or_create_history_retrieval_model()

    context['amountRetrieved'] = historyStatus.amountRetrieved
    context['totalToRetrieve'] = historyStatus.totalToRetrieve
    context['percentageToShow'] = historyStatus.amountRetrieved/historyStatus.totalToRetrieve*100

    return JsonResponse(context)

@login_required
def get_backtest_run_status_api(request):
    
    context = {}

    backtestRun = BasicAnalysisManager.get_or_create_basic_analysis_run_model()

    context['amountRetrieved'] = backtestRun.amountRetrieved
    context['totalToRetrieve'] = backtestRun.totalToRetrieve
    context['percentageToShow'] = backtestRun.amountRetrieved/backtestRun.totalToRetrieve*100

    return JsonResponse(context)

@login_required
def get_all_basic_analyzer_results(request):

    context = {}

    jsonResult = serializers.serialize('json', BasicAnalysisResultsModel.objects.order_by('-roi'))
    context['barResults'] = jsonResult

    return JsonResponse(context)
