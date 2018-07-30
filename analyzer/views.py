import logging
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from managers.ConfigManager import ConfigManager
from managers.HaasManager import HaasManager
from managers.UtilManager import UtilManager

from managers.BasicAnalysisManager import BasicAnalysisManager
from managers.HistoryRetrievalManager import HistoryRetrievalManager

from analyzer.tasks import *

# Create your views here.
@login_required
def basic_analyzer_view(request):

    config = ConfigManager.get_or_create_config()
    history = HistoryRetrievalManager.get_or_create_history_retrieval_model()
    basicAnalysis = BasicAnalysisManager.get_or_create_basic_analysis_run_model()

    context = {'accounts': HaasManager.get_all_accounts(),
                'customBots': HaasManager.get_all_custom_bots(),
                'tradeBots': HaasManager.get_all_trade_bots(),
                'history': HistoryRetrievalManager.get_or_create_history_retrieval_model(),
                'basicAnalysis': BasicAnalysisManager.get_or_create_basic_analysis_run_model()
                }

    if history.completed == True and basicAnalysis.started == False:
        basicAnalysis.started = True
        context['basicAnalysis'] = basicAnalysis
        markets = HaasManager.get_all_markets_for_guid(basicAnalysis.accountGuid)
        BasicAnalysisManager.set_total_to_retrieve(len(markets))
        BasicAnalysisManager.mark_started()

        backtest_all_markets_with_bot(config.haasIp, config.haasPort, config.haasSecret, basicAnalysis.accountGuid, 
            basicAnalysis.botGuid, basicAnalysis.timeFrameInMinutes, "", basicAnalysis.isCustomBot)

    return render(request, 'authed/basic_analyzer.html', context)


@login_required
def start_basic_analyzer_action(request):

    if request.method == "POST":
        accountGuid = request.POST.get('accountselection', '')
        botGuid = request.POST.get('botselection', '')
        timeFrameToTest = request.POST.get('timeframetotest', 1440)

        botGuidSplit = botGuid.split(':')
        
        botType = botGuidSplit[0]
        botGuid = botGuidSplit[1]

        config = ConfigManager.get_or_create_config()
        markets = HaasManager.get_all_markets_for_guid(accountGuid)

        HistoryRetrievalManager.reset_retrieval_info()
        HistoryRetrievalManager.set_retrieval_info(accountGuid, len(markets))

        HistoryRetrievalManager.mark_started()

        BasicAnalysisManager.set_account_guid(accountGuid)
        BasicAnalysisManager.set_bot_guid(botGuid)
        BasicAnalysisManager.set_time_frame_in_minutes(int(timeFrameToTest)*2)

        if botType == "CB":
            BasicAnalysisManager.set_is_custom_bot(True)

        download_history_for_all_markets_task(config.haasIp, config.haasPort, config.haasSecret, accountGuid, int(timeFrameToTest)*2)

        return redirect('/analyzer/basic')
    else:
        print("derp")
        return redirect('/')

@login_required
def reset_basic_analyzer_action(request):

    config = HistoryRetrievalManager.get_or_create_history_retrieval_model()
    basicAnalyzer = BasicAnalysisManager.get_or_create_basic_analysis_run_model()

    config.delete()
    basicAnalyzer.delete()

    BasicAnalysisManager.clear_all_results()

    return redirect('/analyzer/basic')