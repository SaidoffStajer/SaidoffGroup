from django.contrib import admin
from .models import Service, Order, Service_description, Portfolio

# Register your models here.


admin.site.register(Service)
admin.site.register(Order)
admin.site.register(Service_description)
admin.site.register(Portfolio)
