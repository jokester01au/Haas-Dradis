from django.conf.urls import url

from api.views import *

urlpatterns = [
    url(r'^get-history-retrieval-status', get_history_retrieval_status_api, name="get_history_retrieval_status_api"),
    url(r'^get-backtest-run-status', get_backtest_run_status_api, name="get_backtest_run_status_api"),
    url(r'^get-all-basic-analyzer-results', get_all_basic_analyzer_results, name="get_all_basic_analyzer_results")

]
