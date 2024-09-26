from django.contrib import admin
from .models import Faq_category, Faq, Feedback, WhyUs,Partners, Team,Subscribe, Certificate,Feature, Price
from modeltranslation.admin import TranslationAdmin

# Register your models here.

class Faq_categoryAdmin(TranslationAdmin):
    list_display = ('id', 'title')
admin.site.register(Faq_category,Faq_categoryAdmin)


class FaqAdmin(TranslationAdmin):
    list_display = ('id', 'questions', 'faq_page',)
admin.site.register(Faq, FaqAdmin)

class FeedbackAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'comment', 'profession', 'image')
admin.site.register(Feedback, FeedbackAdmin)



class WhyUsAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'description')
admin.site.register(WhyUs, WhyUsAdmin)


class PartnersAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')
admin.site.register(Partners, PartnersAdmin)


class TeamAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'image', 'profession', 'created_at')
admin.site.register(Team, TeamAdmin)


class SubscribeAdmin(TranslationAdmin):
    list_display = ('id', 'full_name', 'phone_number', 'is_checked', 'created_at')
admin.site.register(Subscribe, SubscribeAdmin)


class CertificateAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'description', 'image')
admin.site.register(Certificate, CertificateAdmin)


class FeatureAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'tic')
admin.site.register(Feature, FeatureAdmin)


class PriceAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'price', 'date', 'user',)
admin.site.register(Price, PriceAdmin)

