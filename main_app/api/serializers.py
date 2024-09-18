from rest_framework import serializers
from ..models import *


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
