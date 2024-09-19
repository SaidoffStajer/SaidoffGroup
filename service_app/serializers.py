from rest_framework import serializers
from .models import Service, Order, Service_description, Portfolio

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'title')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'name', 'phone_number', 'service_name', 'message', 'created_at', 'is_checked')


class ServiceDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service_description
        fields = ('id', 'image', 'title', 'description', 'service_typ')



class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ('id', 'image', 'url_link', 'service_name')

