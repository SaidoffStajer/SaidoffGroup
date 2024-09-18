from rest_framework import serializers
from ..models import *


class WhyUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = WhyUs
        fields = "__all__"


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
        fields = "__all__"


class FeedBackSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeedBack
        fields = "__all__"

    
class FAQCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = FAQCategory
        fields = "__all__"

class FAQSerializer(serializers.ModelSerializer):

    class Meta:
        model = FAQ
        fields = "__all__"


