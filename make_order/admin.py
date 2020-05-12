from django.contrib import admin
from .models import Office, Place, Order, Service, ServiceGroup

admin.site.register(Office)
admin.site.register(Service)
admin.site.register(Place)
admin.site.register(Order)
admin.site.register(ServiceGroup)
