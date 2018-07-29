from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from managers.ConfigManager import ConfigManager
from managers.HaasManager import HaasManager
from managers.UtilManager import UtilManager

# Create your views here.
@login_required
def dashboard_view(request):
    context = {}

    # Check to see if haas is working
    haasCheck = HaasManager.haasomeClient.test_credentials()

    if HaasManager.verify_haas_connectivity():

        #Continue
        customBots = HaasManager.get_all_custom_bots()
        tradeBots = HaasManager.get_all_trade_bots()

        context = {'customBots': customBots, 
                   'tradeBots': tradeBots,
                   'amountOfCustomBots': len(customBots),
                   'amountOfTradeBots': len(tradeBots),
                   'totalBotsCount': len(tradeBots) + len(customBots),
                   'totalRoi': UtilManager.get_roi_from_bot_list(tradeBots) + UtilManager.get_roi_from_bot_list(customBots),
                   'totalTradeCount': UtilManager.get_total_trades_from_bot_list(tradeBots) + UtilManager.get_total_trades_from_bot_list(customBots),
                   'totalActivatedBots': UtilManager.get_activated_count_from_bot_list(tradeBots) + UtilManager.get_activated_count_from_bot_list(customBots)}

        if 'successNotification' in request.session:
            context['successNotification'] = request.session['successNotification']

        if 'failureNotification' in request.session:
            context['failureNotification'] = request.session['failureNotification']

        request = UtilManager.clear_session_notifications(request)

    else:
        context = {'connectFailure': True}

    return render(request, 'authed/dashboard.html', context)

@login_required
def setitngs_view(request):
    context = {'config': ConfigManager.get_or_create_config()}
    return render(request, 'authed/settings.html', context)

@login_required
def save_settings_action(request):

    context = {}

    if request.method == "POST":
        haasIp = request.POST.get('haasip', '')
        haasPort = request.POST.get('haasport', 0)
        haasSecret = request.POST.get('haassecret', '')
        numConcurrentTask = request.POST.get('numconcurrenttest', 0)

        ConfigManager.set_haas_configuration(haasIp, haasPort, haasSecret)
        ConfigManager.set_num_concurrent_test(numConcurrentTask)

        if HaasManager.quick_test_haas_creds(haasIp, haasPort, haasSecret):
            context = {'success': True,
            'config': ConfigManager.get_or_create_config()}
            HaasManager.init_haas_manager(haasIp, haasPort, haasSecret)
        else:
            context = {'success': False,
            'config': ConfigManager.get_or_create_config()}

        return render(request, 'authed/settings.html', context)
    else:
        return redirect('/settings')

@login_required
def activate_trade_bot_action(request, botguid):

    context = {}

    if HaasManager.activate_trade_bot_by_guid(botguid):
        request.session['successNotification'] = "Activated Trade Bot: " + botguid
    else:
        request.session['failureNotification'] = "Failed to activate Trade Bot: " + botguid

    return redirect('/')

@login_required
def deactivate_trade_bot_action(request, botguid):

    context = {}

    if HaasManager.deactivate_trade_bot_by_guid(botguid):
        request.session['successNotification'] = "Deactivated Trade Bot: " + botguid
    else:
        request.session['failureNotification'] = "Failed to deactivate Trade Bot: " + botguid

    return redirect('/')

@login_required
def delete_trade_bot_action(request, botguid):

    context = {}

    if HaasManager.delete_trade_bot_by_guid(botguid):
        request.session['successNotification'] = "Deleted Trade Bot: " + botguid
    else:
        request.session['failureNotification'] = "Failed to delete Trade Bot: " + botguid

    return redirect('/')

@login_required
def activate_custom_bot_action(request, botguid):

    context = {}

    if HaasManager.activate_custom_bot_by_guid(botguid):
        request.session['successNotification'] = "Activated Custom Bot: " + botguid
    else:
        request.session['failureNotification'] = "Failed to activate Custom Bot: " + botguid

    return redirect('/')

@login_required
def deactivate_custom_bot_action(request, botguid):

    context = {}

    if HaasManager.deactivate_custom_bot_by_guid(botguid):
        request.session['successNotification'] = "Deactivated Custom Bot: " + botguid
    else:
        request.session['failureNotification'] = "Failed to deactivate Custom Bot: " + botguid

    return redirect('/')

@login_required
def delete_custom_bot_action(request, botguid):

    context = {}

    if HaasManager.delete_custom_bot_by_guid(botguid):
        request.session['successNotification'] = "Deleted Custom Bot: " + botguid
    else:
        request.session['failureNotification'] = "Failed to delete Custom Bot: " + botguid

    return redirect('/')