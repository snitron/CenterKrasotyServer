from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name="main_page"),
    path('chooseOffice/', views.choose_office, name='choose_office'),
    path('chooseService/', views.choose_service, name='choose_service'),
    path('choosePlace/', views.choose_place, name='choose_place'),
    path('chooseTime/', views.choose_time, name='choose_time'),
    path('Finish/', views.create_order, name='create_order')
]
