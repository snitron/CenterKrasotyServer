from uuid import uuid4
from .models import Client, User, SmsCode
import sys
from make_order.models import Office, Place, Order, Service, ServiceGroup
from django.http import HttpResponse

import json

sys.path.append("../")


def index(request):
    return HttpResponse("aaaa")


def registrate(auth_request):
    if auth_request.method == "GET":
        return HttpResponse("No GET requests!")
    data = auth_request.POST
    passw = data.get("password")
    phone = data.get("phone")
    name = data.get("name")
    surname = data.get("surname")
    usrs1 = Client.objects.filter(phone_number__exact=phone)
    usrs2 = Client.objects.filter(phone_number__exact=phone)
    usr1 = 0
    usr2 = 0
    token = str(uuid4())
    code = 0
    for i in usrs1:
        usr1 = i
    for i in usrs2:
        usr2 = i
    if usr1:
        code = 400
        token = usr1.token
    elif usr2:
        code = 403
        token = usr2.token
    else:
        new_user = User(username=phone, password=passw, first_name=name, last_name=surname)
        new_client = Client(user=new_user, password=passw, phone_number=phone, token=token)
        new_user.save()
        new_client.save()
        code = 100
    tmp = {"phone": phone, "token": token, "code": code}
    return HttpResponse(json.dumps(tmp))


def login_user(auth_request):
    if auth_request.method == "GET":
        return HttpResponse("No GET requests!")
    data = auth_request.POST
    phone = data.get("phone")
    passw = data.get("password")
    usrs = Client.objects.filter(phone_number__exact=phone)
    code = 0
    token = 0
    usr = 0
    for i in usrs:
        usr = i
    if not usr:
        code = 401
    elif passw != usr.password:
        code = 401
    else:
        code = 200
        token = usr.token
    tmp = {"phone": phone, "token": token, "code": code}
    return HttpResponse(json.dumps(tmp))


def sms_request(sms_req):
    if sms_req.method == "GET":
        return HttpResponse("No GET requests!")
    data = sms_req.POST
    phone = data.get("phone")
    sms_code = data.get("code")
    attempts = data.get("attempts")
    code = 0
    r_c = SmsCode.objects.get(phone__exact=phone)
    result = str(r_c.code) == str(sms_code)
    if not result:
        if int(attempts) > 3:
            code = 410
        else:
            code = 401
    else:
        code = 200

    tmp = {"phone": phone, "code": code}
    return HttpResponse(json.dumps(tmp))


def send_sms(req):
    data = req.POST
    phone = data.get("phone")
    smss = SmsCode.objects.filter(phone__exact=phone)
    for q in smss:
        q.delete()
    sms_code = SmsCode(code=11111, phone=phone)
    sms_code.save()
    return HttpResponse(json.dumps({"code": 200}))


def autorize(token):
    usrs = Client.objects.filter(token__exact=token)
    usr = 0
    for i in usrs:
        usr = i
    return bool(usr)


def make_order(order_req):
    if order_req.method == "GET":
        return HttpResponse("No GET requests!")
    data = order_req.POST
    token = data.get("token")
    orders = data.get("orders")
    orders = json.loads(orders)
    code = 200
    if autorize(token):
        for order in orders:
            date = order["date"]
            start_time = order["startTime"]
            finish_time = order["finishTime"]
            service = Service.objects.get(id__exact=order["serviceId"])
            cl = Client.objects.get(token__exact=token)
            place = Place.objects.get(id__exact=order["placeId"])
            group = ServiceGroup.objects.get(id__exact=order["groupId"])
            new_order = Order(place=place, phone=cl.phone_number, finish_time=finish_time,
                              start_time=start_time, date=date, group=group, service=service)
            new_order.save()
    else:
        code = 0
    return HttpResponse(json.dumps({"code": code}))


def get_offices(office_req):
    if office_req.method == "GET":
        return HttpResponse("No GET requests!")
    data = office_req.POST
    token = data.get("token")
    city = data.get("city")
    offices = []
    code = 200
    if autorize(token):
        offs = Office.objects.all()
        for off in offs:
            data = {}
            data["id"] = off.id
            data["name"] = off.name
            data["info"] = off.info
            data["address"] = off.address
            data["geoCoordinates"] = off.geo_coords
            data["city"] = off.city
            data["finishTime"] = off.fin_time
            data["startTime"] = off.st_time
            offices.append(data)
    else:
        code = 0
    return HttpResponse(json.dumps({"offices": offices, "code": code}))


def get_services(service_req):
    if service_req.method == "GET":
        return HttpResponse("No GET requests!")
    data = service_req.POST
    token = data.get("token")
    off_id = data.get("officeId")
    code = 200
    services = []
    if autorize(token):
        ofs = Office.objects.get(id__exact=off_id)
        servss = Service.objects.filter(office__exact=ofs)
        for service in servss:
            data = {}
            data["id"] = service.id
            data["groupId"] = service.group.id
            data["groupName"] = service.group.name
            data["name"] = service.name
            data["info"] = service.info
            data["price"] = service.price
            data["long"] = service.long
            services.append(data)
    else:
        code = 0
    return HttpResponse(json.dumps({"services": services, "code": code}))


def get_places(place_req):
    if place_req.method == "GET":
        return HttpResponse("No GET requests!")
    data = place_req.POST
    token = data.get("token")
    groupId = data.get("groupId")
    code = 200
    places = []
    if autorize(token):
        pcs = Place.objects.filter(group__exact=groupId)
        for pc in pcs:
            data = {}
            data["id"] = pc.id
            data["info"] = pc.info
            data["image"] = "static/images/" + pc.image.name.split("/")[-1]
            places.append(data)
    else:
        code = 0
    return HttpResponse(json.dumps({"places": places, "code": code}))


def get_orders(order_req):
    if order_req.method == "GET":
        return HttpResponse("No GET requests!")
    data = order_req.POST
    token = data.get("token")
    code = 200
    orders = []
    cl = Client.objects.get(token__exact=token)
    date = 0
    count = 0
    if autorize(token):
        ords = -1
        if data.get("forUser") == 'true':
            ords = Order.objects.filter(phone__exact=cl.phone_number)
        else:
            date = data.get("date")
            group_id = data.get("groupId")
            ords = Order.objects.filter(group__exact=group_id, date__exact=date)
            count = len(Place.objects.filter(group__exact=group_id))
        for ord in ords:
            data = {}
            data["id"] = ord.id
            data["startTime"] = ord.start_time
            data["finishTime"] = ord.finish_time
            data["phone"] = ord.phone
            data["placeId"] = ord.place.id
            data["name"] = ord.service.name
            data["price"] = ord.service.price
            data["date"] = ord.date
            data["images"] = "static/images/" + ord.place.image.name.split("/")[-1]
            data["placeInfo"] = ord.place.info
            orders.append(data)
    else:
        code = 0
    return HttpResponse(json.dumps({"orders": orders, "code": code, "count": count}))


def get_user(request):
    if request.method == "GET":
        return HttpResponse("No GET requests!")
    data = request.POST
    token = data.get("token")
    code = 200
    resp = {}
    if autorize(token):
        clients = Client.objects.filter(token__exact=token)
        client = -1
        for i in clients:
            client = i
        users = User.objects.filter(client__exact=client)
        user = -1
        for i in users:
            user = i
        resp["name"] = user.first_name
        resp["surname"] = user.last_name
    else:
        code = 0
    resp["code"] = code
    return HttpResponse(json.dumps(resp))


def delete_order(request):
    if request.method == "GET":
        return HttpResponse("No GET requests!")
    data = request.POST
    token = data.get("token")
    code = 0
    if autorize(token):
        code = 200
        od = data.get("orderId")
        ord = Order.objects.get(id__exact=int(od))
        ord.delete()
    return HttpResponse(json.dumps({"code": code}))
