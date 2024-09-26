from rest_framework import serializers
from .models import Faq_category, Faq, Feedback, WhyUs,Partners, Team,Subscribe, Certificate, Feature, Price

class Faq_categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq_category
        fields = ('id', 'title_uz', 'title_en', 'title_ru',)

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = ('id', 'questions','questions_en', 'questions_ru', 'answers','answers_en','answers_ru', 'faq_page', 'faq')

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('id', 'name','name_en', 'name_ru', 'comment','comment_en', 'comment_ru' ,'profession', 'image')

class WhyUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyUs
        fields = ('id', 'title','title_en', 'title_ru', 'description', 'description_en', 'description_ru' )

class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = ('id', 'image')

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name','name_en', 'name_ru', 'image', 'profession','profession_en','profession_ru', 'created_at')

class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = ('id', 'full_name','full_name_en','full_name_ru', 'phone_number', 'is_checked', 'created_at')
    
class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ('id', 'title','title_en','title_ru', 'description','description_en','description_ru', 'image')


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ('id', 'title','title_en','title_ru', 'tic' )


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ('id', 'title','title_en','title_ru', 'price', 'date', 'user', 'features')

