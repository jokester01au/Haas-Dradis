from django.contrib import admin

from analyzer.models import HistoryRetrievalModel
from analyzer.models import BasicAnalysisRunModel
from analyzer.models import BasicAnalysisResultsModel

# Register your models here.
admin.site.register(HistoryRetrievalModel)
admin.site.register(BasicAnalysisRunModel)
admin.site.register(BasicAnalysisResultsModel)
