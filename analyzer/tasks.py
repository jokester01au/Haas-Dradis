import time
import logging

from huey import crontab
from huey.contrib.djhuey import periodic_task, task
from huey.contrib.djhuey import db_periodic_task, db_task

from managers.HaasManager import HaasManager
from managers.UtilManager import *

from managers.BasicAnalysisManager import BasicAnalysisManager
from managers.HistoryRetrievalManager import HistoryRetrievalManager

from haasomeapi.enums.EnumPriceSource import EnumPriceSource

def safeHistoryGet(pricesource: EnumPriceSource, primarycurrency: str, secondarycurrency: str, contractname: str, interval: int, depth: int):

    history = None
    historyResult = False
    failCount = 0

    while historyResult == False:
        history = HaasManager.haasomeClient.marketDataApi.get_history(pricesource, primarycurrency, secondarycurrency, contractname, interval, depth)
        if len(history.result) > 1:
            historyResult = True
        else:
            failCount = failCount + 1
            time.sleep(1)

        if failCount == 60:
            historyResult = True

    return history.result

@db_task()
def download_history_for_all_markets_task(haasip: str, haasport: int, haassecret: str, accountguid: str, depth: int):
    
    logging.info("Started the download all market history for exchange task")

    HaasManager.init_haas_manager(haasip, haasport, haassecret)

    historyTasks = {}
    historyResults = {}

    count = 0

    markets = HaasManager.get_all_markets_for_guid(accountguid)

    for market in markets:
        task = download_history_for_market_task(haasip, haasport, haassecret, market.priceSource,
            market.primaryCurrency, market.secondaryCurrency, "", 1, depth)
        historyTasks[count] = task
        count = count + 1

    lastUpdateCount = 0

    while len(historyResults) != len(historyTasks):
        for k, v in historyTasks.items():
            result = v.get()
            if result != None:
                if k in historyResults:
                    pass
                else:
                    historyResults[k] = result

        if len(historyResults) > lastUpdateCount:
            HistoryRetrievalManager.update_amount_retrieved(len(historyResults))
            lastUpdateCount = len(historyResults)

        time.sleep(1)

    HistoryRetrievalManager.mark_completed()

    logging.info("Completed the download all market history for exchange task")

@task()
def download_history_for_market_task(haasip: str, haasport: int, haassecret: str, pricesource: EnumPriceSource, primarycurrency: str, 
    secondarycurrency: str, contractname: str, interval: int, depth: int):

    logging.info("Started the download history for " + primarycurrency + "/" + secondarycurrency)

    HaasManager.init_haas_manager(haasip, haasport, haassecret)

    history = safeHistoryGet(pricesource, primarycurrency, secondarycurrency, contractname, interval, depth)

    logging.info("Completed the download history for " + primarycurrency + "/" + secondarycurrency)

    return history

@db_task()
def backtest_all_markets_with_bot(haasip: str, haasport: int, haassecret: str, accountguid: str, botguid: str, timeframeinminutes: int, contractname: str, iscustombot: bool):
    
    logging.info("Started the backtest of all markets")

    HaasManager.init_haas_manager(haasip, haasport, haassecret)

    backtestTasks = {}
    backtestResults = {}

    count = 0

    markets = HaasManager.get_all_markets_for_guid(accountguid)

    accountInfo = HaasManager.get_account_info_for_id(accountguid)

    baseBotInfo = None

    if iscustombot:
        baseBotInfo = HaasManager.get_custom_bot_by_id(botguid)
    else:
        baseBotInfo = HaasManager.get_trade_bot_by_id(botguid)

    logging.info(baseBotInfo)
    logging.info(baseBotInfo.name)

    for market in markets:
        task = None

        if iscustombot:
            task = backtest_custom_bot_on_market(haasip, haasport, haassecret, accountguid, botguid, 
                timeframeinminutes, market.primaryCurrency, market.secondaryCurrency, contractname)
        else: 
            task = backtest_trade_bot_on_market(haasip, haasport, haassecret, accountguid, botguid, 
                timeframeinminutes, market.primaryCurrency, market.secondaryCurrency, contractname)

        backtestTasks[count] = task
        count = count + 1

    lastUpdateCount = 0

    while len(backtestResults) != len(backtestTasks):
        for k, v in backtestTasks.items():
            result = v.get()
            if result != None:
                if k in backtestResults:
                    pass
                else:
                    backtestResults[k] = result
                    BasicAnalysisManager.create_basic_analysis_results_model(accountguid, EnumPriceSource(accountInfo.connectedPriceSource).name, botguid, baseBotInfo.name, result.priceMarket.primaryCurrency, result.priceMarket.secondaryCurrency, 
                        result.roi, iscustombot)

        if len(backtestResults) > lastUpdateCount:
            BasicAnalysisManager.update_amount_retrieved(len(backtestResults))
            lastUpdateCount = len(backtestResults)

        time.sleep(1)

    BasicAnalysisManager.mark_completed()

    logging.info("Completed the backtest of all markets task")

@task()
def backtest_trade_bot_on_market(haasip: str, haasport: int, haassecret: str, accountguid: str, botguid: str, timeframeinminutes: int, primarycurrency: str, 
    secondarycurrency: str, contractname: str):

    logging.info("Started backtest on pair  " + primarycurrency + "/" + secondarycurrency)

    HaasManager.init_haas_manager(haasip, haasport, haassecret)
    
    accountInfo = HaasManager.haasomeClient.accountDataApi.get_account_details(accountguid).result

    backTestResult = HaasManager.haasomeClient.customBotApi.backtest_custom_bot_on_market(accountguid, botguid, timeframeinminutes, primarycurrency, secondarycurrency, contractname)

    return backTestResult.result

@task()
def backtest_custom_bot_on_market(haasip: str, haasport: int, haassecret: str, accountguid: str, botguid: str, timeframeinminutes: int, primarycurrency: str, 
    secondarycurrency: str, contractname: str):

    logging.info("Started backtest on pair  " + primarycurrency + "/" + secondarycurrency)

    HaasManager.init_haas_manager(haasip, haasport, haassecret)
    
    accountInfo = HaasManager.haasomeClient.accountDataApi.get_account_details(accountguid).result

    # Create Template Bot
    backTestResult = HaasManager.haasomeClient.customBotApi.backtest_custom_bot_on_market(accountguid, botguid, timeframeinminutes, primarycurrency, secondarycurrency, contractname)

    return backTestResult.result