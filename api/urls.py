from django.conf.urls import url

from api.views import *

urlpatterns = [
    url(r'^get-history-retrieval-status', get_history_retrieval_status_api, name="get_history_retrieval_status_api"),

]
