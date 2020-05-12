from django.urls import path
from . import views

#пути для API
urlpatterns = [
    path('', views.index, name='index'),
    path('registerNewUser/', views.registrate, name='registrate'),
    path('loginByPass/', views.login_user, name='login'),
    path('smsRequest/', views.sms_request, name='sms_req'),
    path('addTransaction/', views.make_order, name='make_order'),
    path('getOffices/', views.get_offices, name='get_offices'),
    path('getServices/', views.get_services, name='get_services'),
    path('getPlaces/', views.get_places, name='get_places'),
    path('getOrders/', views.get_orders, name='get_orders'),
    path('getUser/', views.get_user, name='get_user'),
    path('deleteOrder/', views.delete_order, name='delete_order'),
    path('sendNewSms/', views.send_sms, name='send_sms')
]
