import logging
import datetime
from django import template

from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
from haasomeapi.enums.EnumPriceSource import EnumPriceSource

from managers.HaasManager import HaasManager

register = template.Library()


@register.filter(name='int_time_to_datetime')
def int_time_to_datetime(timetochange: int):
    return datetime.datetime.fromtimestamp(timetochange)

@register.filter(name='bot_type_num_to_str')
def bot_type_num_to_str(bottypenum: int):
    return EnumCustomBotType(bottypenum).name

@register.filter(name='price_source_num_to_str')
def price_source_num_to_str(pricesourcenum: int):
    return EnumPriceSource(pricesourcenum).name

@register.filter(name='account_id_to_name')
def account_id_to_name(accountid: int):
    return HaasManager.get_account_info_for_id(accountid).name