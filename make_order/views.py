from django.shortcuts import render
from django.http import HttpResponse
from .models import Office, Service, Place, Order, ServiceGroup
import datetime


def get_today_date():
    today = datetime.datetime.today()
    yr = str(today.year)
    month = str(today.month)
    if int(month) < 10:
        month = "0" + month
    day = str(today.day)
    if int(day) < 10:
        day = "0" + day
    today = yr + "-" + month + "-" + day
    return today


def from_str_to_minute(time):
    time = time.split(":")
    return int(time[0]) * 60 + int(time[1])


def from_minute_to_str(minute):
    h = minute // 60
    if h < 10:
        h = "0" + str(h)
    h = str(h)
    m = minute % 60
    if m < 10:
        m = "0" + str(m)
    m = str(m)
    return h + ":" + m


def main_page(request):
    return render(request, "main_page.html")


def choose_office(request):
    offices = Office.objects.all()
    return render(request, "choose_office.html", {"offices": offices})


def choose_service(request):
    o_id = request.GET.get("id")
    services = Service.objects.filter(office__exact=o_id)
    return render(request, "choose_service.html", {"services": services})


def choose_place(request):
    s_id = request.GET.get("serviceId")
    tm = request.GET.get("time")
    time = from_str_to_minute(tm)
    service = Service.objects.get(id__exact=s_id)
    places = []
    today = get_today_date()
    ords = Order.objects.filter(date__exact=today, group__exact=service.group)
    for place in Place.objects.filter(group__exact=service.group):
        for order in ords:
            st = from_str_to_minute(order.start_time)
            fn = from_str_to_minute(order.finish_time)
            if order.place == place and not (time + service.long < st or time > fn):
                break
        else:
            places.append(place)
    return render(request, "choose_place.html", {"places": places, "time": tm, "service": service})


def choose_time(request):
    s_id = request.GET.get("id")
    service = Service.objects.get(id__exact=s_id)
    st = from_str_to_minute(service.office.st_time)
    fn = from_str_to_minute(service.office.fin_time)
    today = get_today_date()
    ords = Order.objects.filter(date__exact=today, group__exact=service.group)
    times = {}
    count = len(Service.objects.filter(group_id__exact=service.group_id))
    for time in range(st, fn - service.long, 30):
        times[time] = []
        for order in ords:
            st_time = from_str_to_minute(order.start_time)
            fn_time = from_str_to_minute(order.finish_time)
            if time > fn_time or (time + service.long) < st_time:
                break
            else:
                times[time].append(-1)
        if len(times[time]) == count:
            del times[time]
    times = list(times.keys())
    for i in range(len(times)):
        times[i] = from_minute_to_str(times[i])

    return render(request, "choose_time.html", {"times": times, "serviceId": service.id})


def create_order(request):
    place = Place.objects.get(id__exact=request.GET.get("place"))
    time = request.GET.get("time")
    service = Service.objects.get(id__exact=request.GET.get("service"))
    phone = request.user.username
    ftime = from_minute_to_str(from_str_to_minute(time) + service.long)
    date = get_today_date()
    new_order = Order(phone=phone, start_time=time, finish_time=ftime, date=date, group=service.group, place=place)
    new_order.save()
    return render(request, "finish.html")
