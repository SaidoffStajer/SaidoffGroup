from django.shortcuts import render
from .models import Faq_category, Faq, Feedback, WhyUs,Partners, Team,Subscribe, Certificate, Feature, Price
from .serializers import Faq_categorySerializer,FaqSerializer, FeedbackSerializer, WhyUsSerializer, PartnersSerializer, TeamSerializer, SubscribeSerializer, CertificateSerializer,FeatureSerializer,PriceSerializer
from rest_framework import generics

# Create your views here.

class Faq_categoryList(generics.ListCreateAPIView):
    queryset = Faq_category.objects.all()
    serializer_class = Faq_categorySerializer

class FaqList(generics.ListCreateAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer

class FeedbackList(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class WhyUsList(generics.ListCreateAPIView):
    queryset = WhyUs.objects.all()
    serializer_class = WhyUsSerializer

class PartnersList(generics.ListCreateAPIView):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer

class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class SubscribeList(generics.ListCreateAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer

class CertificateList(generics.ListCreateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

class Faq_categoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Faq_category.objects.all()
    serializer_class = Faq_categorySerializer

class FaqDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer

class FeedbackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class WhyUsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WhyUs.objects.all()
    serializer_class = WhyUsSerializer

class PartnersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer

class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class SubscribeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer

class CertificateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class FeatureList(generics.ListCreateAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


class PriceList(generics.ListCreateAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class FeatureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


class PriceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer





