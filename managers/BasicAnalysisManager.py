from analyzer.models import BasicAnalysisRunModel
from analyzer.models import BasicAnalysisResultsModel


class BasicAnalysisManager:

    @staticmethod
    def get_or_create_basic_analysis_run_model():
        try:
            barModel = BasicAnalysisRunModel.objects.get()
            return barModel

        except:
            barModel = BasicAnalysisRunModel()
            barModel.save()
            return barModel

    @staticmethod
    def reset_retrieval_info():
        barModel = BasicAnalysisManager.get_or_create_basic_analysis_run_model()
        barModel.accountGuid = ""
        barModel.amountRetrieved = 0
        barModel.totalToRetrieve = 0
        barModel.started = False
        barModel.completed = False
        barModel.save()       

    @staticmethod
    def set_retrieval_info(accountguid: str, totaltoretrieve: int):
        barModel = BasicAnalysisManager.get_or_create_basic_analysis_run_model()
        barModel.accountGuid = accountguid
        barModel.amountRetrieved = 0
        barModel.totalToRetrieve = totaltoretrieve
        barModel.save()

    @staticmethod
    def set_is_custom_bot(iscustombot: bool):
        barModel = BasicAnalysisManager.get_or_create_basic_analysis_run_model()
        barModel.isCustomBot = iscustombot
        barModel.save()
    
    @staticmethod
    def set_total_to_retrieve(totaltoretrieve: int):
        barModel = BasicAnalysisManager.get_or_create_basic_analysis_run_model()
        barModel.totalToRetrieve = totaltoretrieve
        barModel.save()

    @staticmethod
    def set_account_guid(accountguid: str):
        barModel = BasicAnalysisManager.get_or_create_basic_analysis_run_model()
        barModel.accountGuid = accountguid
        barModel.save()

    @staticmethod
    def set_bot_guid(botguid: str):
        barModel = BasicAnalysisManager.get_or_create_basic_analysis_run_model()
        barModel.botGuid = botguid
        barModel.save()

    @staticmethod
    def set_time_frame_in_minutes(timeframeinminutes: int):
        barModel = BasicAnalysisManager.get_or_create_basic_analysis_run_model()
        barModel.timeFrameInMinutes = timeframeinminutes
        barModel.save()

    @staticmethod
    def update_amount_retrieved(amountretrieved: int):
        barModel = BasicAnalysisManager.get_or_create_basic_analysis_run_model()
        barModel.amountRetrieved = amountretrieved
        barModel.save() 

    @staticmethod
    def mark_started():
        barModel = BasicAnalysisManager.get_or_create_basic_analysis_run_model()
        barModel.started = True
        barModel.save()

    @staticmethod
    def mark_completed():
        barModel = BasicAnalysisManager.get_or_create_basic_analysis_run_model()
        barModel.completed = True
        barModel.save()

    @staticmethod
    def create_basic_analysis_results_model(accountguid: str, exchangeName: str, basebotguid: str, basebotname: str, primarycurrency: str, secondarycurrency: str, roi: float, iscustombot: bool):
        barModel = BasicAnalysisResultsModel()
        barModel.accountGuid = accountguid
        barModel.exchangeName = exchangeName
        barModel.baseBotGuid = basebotguid
        barModel.primaryCurrency = primarycurrency
        barModel.secondaryCurrency = secondarycurrency
        barModel.roi = roi
        barModel.isCustomBot = iscustombot
        barModel.save()

    @staticmethod
    def clear_all_results():
        BasicAnalysisResultsModel.objects.all().delete()