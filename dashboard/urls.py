from django.conf.urls import url

from dashboard.views import *


urlpatterns = [
    url(r'^$', dashboard_view, name="dashboard_view"),
    url(r'^settings', setitngs_view, name="setitngs_view"),
    url(r'^save-settings', save_settings_action, name="save_settings_action"),
    url(r'^activate-trade-bot/(?P<botguid>.+)', activate_trade_bot_action, name="activate_trade_bot_action"),
    url(r'^deactivate-trade-bot/(?P<botguid>.+)', deactivate_trade_bot_action, name="deactivate_trade_bot_action"),
    url(r'^delete-trade-bot/(?P<botguid>.+)', delete_trade_bot_action, name="delete_trade_bot_action"),
    url(r'^activate-custom-bot/(?P<botguid>.+)', activate_custom_bot_action, name="activate_custom_bot_action"),
    url(r'^deactivate-custom-bot/(?P<botguid>.+)', deactivate_custom_bot_action, name="deactivate_custom_bot_action"),
    url(r'^delete-custom-bot/(?P<botguid>.+)', delete_custom_bot_action, name="delete_custom_bot_action")
]
