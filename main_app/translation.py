from modeltranslation.translator import TranslationOptions, translator
from .models import WhyUs, Certificate,FeedBack,FAQ

class WhyUsTranslation(TranslationOptions):
    fields = ('title', 'description')

class CertificateTranslation(TranslationOptions):
    fields = ('title','description')

class FeedBackTranslation(TranslationOptions):
    fields = ('comment',)

class FAQTransaltion(TranslationOptions):
    fields = ('answer','question')



for a,b in [(Certificate,CertificateTranslation),(WhyUs, WhyUsTranslation),(FeedBack,FeedBackTranslation),(FAQ,FAQTransaltion)]:
    translator.register(a,b)

