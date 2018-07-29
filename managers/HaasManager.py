import logging
from haasomeapi.HaasomeClient import HaasomeClient

from haasomeapi.enums.EnumErrorCode import EnumErrorCode

class HaasManager:

    haasomeClient = HaasomeClient("","")

    @staticmethod
    def init_haas_manager(ip: str, port: int, secret: str):
        ipport = "http://"+ip+":"+str(port)
        HaasManager.haasomeClient = HaasomeClient(ipport, secret)

    @staticmethod
    def quick_test_haas_creds(ip: str, port: int, secret: str):
        ipport = "http://"+ip+":"+str(port)
        haasClient = HaasomeClient(ipport, secret)

        testCall = haasClient.test_credentials()

        if testCall.errorCode == EnumErrorCode.SUCCESS:
            return True
        else:
            logging.error(testCall.errorMessage)
            return False

    @staticmethod
    def verify_haas_connectivity():

        testCall = HaasManager.haasomeClient.test_credentials()

        if testCall.errorCode == EnumErrorCode.SUCCESS:
            return True
        else:
            return False

    @staticmethod
    def display_accounts():
        Util.get_logger().info("Please Set One Of the guids in the config file")
        accounts = HaasManager.haasomeClient.accountDataApi.get_all_account_details()

        if accounts.errorCode == EnumErrorCode.SUCCESS:
            for k,v in accounts.result.items():
                print(v.name + " - " + v.guid)
        else:
            logging.error("Could not retrieve account information")

    @staticmethod
    def check_account_guid(accountguid: str):

        account = HaasManager.haasomeClient.accountDataApi.get_account_details(accountguid)

        if account.errorCode == EnumErrorCode.SUCCESS:
            return True

        return False

    @staticmethod
    def activate_trade_bot_by_guid(botguid: str):
        
        apiCommand = HaasManager.haasomeClient.tradeBotApi.activate_trade_bot(botguid, False)

        if apiCommand.errorCode == EnumErrorCode.SUCCESS:
            return True
        else:
            logging.error(apiCommand.errorMessage)

        return False

    @staticmethod
    def deactivate_trade_bot_by_guid(botguid: str):

        apiCommand = HaasManager.haasomeClient.tradeBotApi.deactivate_trade_bot(botguid, False)

        if apiCommand.errorCode == EnumErrorCode.SUCCESS:
            return True
        else:
            logging.error(apiCommand.errorMessage)

        return False

    @staticmethod
    def delete_trade_bot_by_guid(botguid: str):

        apiCommand = HaasManager.haasomeClient.tradeBotApi.remove_trade_bot(botguid, False)

        if apiCommand.errorCode == EnumErrorCode.SUCCESS:
            return True
        else:
            logging.error(apiCommand.errorMessage)

        return False

    @staticmethod
    def activate_custom_bot_by_guid(botguid: str):
        
        apiCommand = HaasManager.haasomeClient.customBotApi.activate_custom_bot(botguid, False)

        if apiCommand.errorCode == EnumErrorCode.SUCCESS:
            return True
        else:
            logging.error(apiCommand.errorMessage)

        return False

    @staticmethod
    def deactivate_custom_bot_by_guid(botguid: str):

        apiCommand = HaasManager.haasomeClient.customBotApi.deactivate_custom_bot(botguid, False)

        if apiCommand.errorCode == EnumErrorCode.SUCCESS:
            return True
        else:
            logging.error(apiCommand.errorMessage)

        return False

    @staticmethod
    def delete_custom_bot_by_guid(botguid: str):

        apiCommand = HaasManager.haasomeClient.customBotApi.remove_custom_bot(botguid, False)

        if apiCommand.errorCode == EnumErrorCode.SUCCESS:
            return True
        else:
            logging.error(apiCommand.errorMessage)

        return False

    @staticmethod
    def get_open_orders(accountguid: str):

        openOrders = HaasManager.haasomeClient.accountDataApi.get_all_open_orders()

        if openOrders.errorCode == EnumErrorCode.SUCCESS:
            return openOrders.result
        else:
            logging.error("Failed to retrieve open orders")
            return None

    @staticmethod
    def get_order_status(orderid: str):

        order = HaasManager.haasomeClient.accountDataApi.get_template_status(orderid)

        if order.errorCode == EnumErrorCode.SUCCESS:
            return order.result

        else:
            return None

    @staticmethod
    def get_all_custom_bots():

        results = []

        customBots = HaasManager.haasomeClient.customBotApi.get_all_custom_bots()

        if customBots.errorCode == EnumErrorCode.SUCCESS:
            
            for customBot in customBots.result:
                if 'Dradis' in customBot.name:
                    pass
                else:
                    results.append(customBot)

            return results
        else:
            logging.error(customBots.errorMessage)
            return []

    @staticmethod
    def get_all_trade_bots():

        results = []

        tradeBots = HaasManager.haasomeClient.tradeBotApi.get_all_trade_bots()

        if tradeBots.errorCode == EnumErrorCode.SUCCESS:

            for tradeBot in tradeBots.result:
                if 'Dradis' in tradeBot.name:
                    pass
                else:
                    results.append(tradeBot)

            return results
        else:
            logging.error(tradeBots.errorMessage)
            return []

    @staticmethod
    def get_account_info_for_id(accountid: int):
        accountInfo = HaasManager.haasomeClient.accountDataApi.get_account_details(accountid)

        if accountInfo.errorCode == EnumErrorCode.SUCCESS:
            return accountInfo.result
        else:
            logging.error(accountInfo.errorMessage)
            return []

