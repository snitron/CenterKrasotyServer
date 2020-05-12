from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login
import sys
from api.models import Client
from uuid import uuid4
from django.http import HttpResponseRedirect

sys.path.append("../")


def register_view(request):
    if request.method == "POST":
        token = str(uuid4())
        phone = request.POST['phone']
        password = request.POST['password']
        password_rep = request.POST['password_rep']
        name = request.POST['name']
        surname = request.POST['surname']
        new_user = User.objects.create_user(username=phone, password=password, first_name=name, last_name=surname)
        new_client = Client(user=new_user, phone_number=phone, token=token, password=password)
        new_user.save()
        new_client.save()
        login(request=request, user=new_user)
        return HttpResponseRedirect("../")
    return render(request, "register.html")
