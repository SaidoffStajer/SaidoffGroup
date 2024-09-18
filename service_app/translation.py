from modeltranslation.translator import TranslationOptions, translator
from .models import ServiceDescription, Service


class ServiceTranslation(TranslationOptions):
    fields = ('title',)


class ServiceDescriptionTranslation(TranslationOptions):
    fields = ('title','description')

translator.register(ServiceDescription, ServiceDescriptionTranslation)
translator.register(Service, ServiceTranslation)
