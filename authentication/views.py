from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate


def login_view(request):

    context = {}

    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            context["error"] = True
            return render(request, 'public/login.html', context)
    else:
        return render(request, 'public/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')
# Create your views here.
