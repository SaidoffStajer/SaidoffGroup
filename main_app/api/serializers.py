from rest_framework import serializers
from ..models import *
from django.utils.translation import get_language

class WhyUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = WhyUs
        fields = (
            'title', 'title_en', 'title_uz', 'title_ru','description' ,
            'description_en', 'description_ru', 'description_uz'
        )


class PartnersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partners
        fields = "__all__"

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = "__all__"


class SubscribeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscribe
        fields = "__all__"


class CertificateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Certificate
        fields = ('image', 'title', 'title_en', 'title_uz', 'title_ru','description' ,
            'description_en', 'description_ru', 'description_uz')


class FeedBackSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeedBack
        fields = ('comment','comment_uz','comment_ru','comment_en','name','image','profession')

    
class FAQCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = FAQCategory
        fields = "__all__"

class FAQSerializer(serializers.ModelSerializer):

    class Meta:
        model = FAQ
        fields = ('faq_page','answer','answer_uz','answer_ru',
                  'answer_en','question','question_uz','question_ru','question_en')



class PricePlanSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PricePlan
        fields = ('title','limit_date','limit_user','features')

    def to_representation(self, instance):

        # Get the default language
        default_language = get_language()
        data = super().to_representation(instance)

        # If you want to manually remove fields in case Modeltranslation adds others
        for field in list(data.keys()):
            # Remove fields that are translations
            if field.endswith(f"_{default_language}"):
                del data[field]

        return data


class FeaturesSerizalizer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ('title','title_en','title_uz','title_ru','tick')