
class UtilManager:

    @staticmethod
    def get_roi_from_bot_list(botlist: any):
        
        totalRoi = 0

        for bot in botlist:
            totalRoi = totalRoi + bot.roi

        return totalRoi

    @staticmethod
    def get_total_trades_from_bot_list(botlist: any):

        totalTrades = 0

        for bot in botlist:
            totalTrades = totalTrades + len(bot.completedOrders)

        return totalTrades

    @staticmethod
    def get_activated_count_from_bot_list(botlist: any):

        totalActivated = 0

        for bot in botlist:
            if bot.activated:
                totalActivated = totalActivated + 1

        return totalActivated

    @staticmethod
    def clear_session_notifications(request: any):

        if 'successNotification' in request.session:
            del request.session['successNotification']

        if 'failureNotification' in request.session:
            del request.session['failureNotification']

        return request

