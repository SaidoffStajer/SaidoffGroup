from django.shortcuts import render
from.models import Service, Order, Service_description, Portfolio,Tag
from .serializers import ServiceSerializer, PortfolioSerializer,OrderSerializer, ServiceDescriptionSerializer, TagSerializer
from rest_framework import generics

# Create your views here.

class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class PortfolioList(generics.ListCreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ServiceDescriptionList(generics.ListCreateAPIView):
    queryset = Service_description.objects.all()
    serializer_class = ServiceDescriptionSerializer

class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class PortfolioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ServiceDescriptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service_description.objects.all()
    serializer_class = ServiceDescriptionSerializer


class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


