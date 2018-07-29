from django.conf.urls import url

from analyzer.views import *

urlpatterns = [
    url(r'^basic', basic_analyzer_view, name="basic_analyzer_view"),
    url(r'^start-basic', start_basic_analyzer_action, name="start_basic_analyzer_action")
]
