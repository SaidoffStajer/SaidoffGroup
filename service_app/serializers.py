from rest_framework import serializers
from .models import Service, Order, Service_description, Portfolio, Tag

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'title','title_en', 'title_ru')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'name', 'name_en', 'name_ru', 'phone_number', 'service_name', 'message', 'created_at', 'is_checked')

class ServiceDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service_description
        fields = ('id', 'image', 'title','title_en','title_ru','description', 'description_en', 'description_ru', 'service_typ')

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ('id', 'image', 'url_link', 'service_name')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'name_en', 'name_ru')

