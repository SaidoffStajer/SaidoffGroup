from django.contrib import admin
from .models import Service, Order, Service_description,Tag
from modeltranslation.admin import TranslationAdmin

# Register your models here.

class ServiceAdmin(TranslationAdmin):
    list_display = ('title',)
admin.site.register(Service,ServiceAdmin)

class OrderAdmin(TranslationAdmin):
    list_display = ('name',)
admin.site.register(Order, OrderAdmin)

class ServiceDescriptionAdmin(TranslationAdmin):
    list_display = ('title', 'description')
admin.site.register(Service_description, ServiceDescriptionAdmin)

class TagAdmin(TranslationAdmin):
    list_display = ('name',)
admin.site.register(Tag, TagAdmin)


