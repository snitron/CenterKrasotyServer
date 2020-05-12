from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # login = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    token = models.CharField(max_length=40, default="null")

    def __str__(self):
        return self.user.username


class SmsCode(models.Model):
    code = models.IntegerField()
    phone = models.CharField(max_length=20, default="0")

    def __str__(self):
        return self.phone
