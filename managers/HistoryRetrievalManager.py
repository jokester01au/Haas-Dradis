from analyzer.models import HistoryRetrievalModel


class HistoryRetrievalManager:

    @staticmethod
    def get_or_create_history_retrieval_model():
        try:
            historyModel = HistoryRetrievalModel.objects.get()
            return historyModel

        except:
            historyModel = HistoryRetrievalModel()
            historyModel.save()
            return historyModel

    @staticmethod
    def reset_retrieval_info():
        historyModel = HistoryRetrievalManager.get_or_create_history_retrieval_model()
        historyModel.accountGuid = ""
        historyModel.amountRetrieved = 0
        historyModel.totalToRetrieve = 0
        historyModel.started = False
        historyModel.completed = False
        historyModel.save()       

    @staticmethod
    def set_retrieval_info(accountguid: str, totaltoretrieve: int):
        historyModel = HistoryRetrievalManager.get_or_create_history_retrieval_model()
        historyModel.accountGuid = accountguid
        historyModel.amountRetrieved = 0
        historyModel.totalToRetrieve = totaltoretrieve
        historyModel.save()

    @staticmethod
    def update_amount_retrieved(amountretrieved: int):
        historyModel = HistoryRetrievalManager.get_or_create_history_retrieval_model()
        historyModel.amountRetrieved = amountretrieved
        historyModel.save() 

    @staticmethod
    def mark_started():
        historyModel = HistoryRetrievalManager.get_or_create_history_retrieval_model()
        historyModel.started = True
        historyModel.save()

    @staticmethod
    def mark_completed():
        historyModel = HistoryRetrievalManager.get_or_create_history_retrieval_model()
        historyModel.completed = True
        historyModel.save()