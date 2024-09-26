from modeltranslation.translator import register, TranslationOptions
from .models import Service, Order, Service_description, Tag

@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Order)
class OrderTranslationOptions(TranslationOptions):
    fields = ('name', )

@register(Service_description)
class ServiceDescriptionTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ("name",)





