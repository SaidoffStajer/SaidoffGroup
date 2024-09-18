from django.contrib import admin
from .models import WhyUs, Partners, Certificate, Subscribe, FAQ, FAQCategory, Team, FeedBack


for a in [WhyUs, Partners, Certificate, Subscribe, FAQ, FAQCategory, Team, FeedBack]:
    admin.site.register(a)

    
