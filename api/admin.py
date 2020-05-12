from django.contrib import admin
from .models import Client, SmsCode

admin.site.register(Client)
admin.site.register(SmsCode)
