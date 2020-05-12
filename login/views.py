from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect


def login_view(request):
    error = " "
    if request.method == "POST":
        phone = request.POST['phone']
        password = request.POST['password']
        user = authenticate(username=phone, password=password)
        if user is not None:
            if user.is_active:
                login(request=request, user=user)
                return HttpResponseRedirect("../")
            else:
                error = "Account is disabled"
        else:
            error = "Неверный логин/пароль"
    return render(request, "login.html", {"error": error})
