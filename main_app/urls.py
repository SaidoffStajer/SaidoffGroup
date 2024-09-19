from django.urls import path
from .views import Faq_categoryList, Faq_categoryDetail, FeedbackList, FeedbackDetail,FaqList, FaqDetail, WhyUsList, WhyUsDetail, PartnersList, PartnersDetail,TeamList,TeamDetail, SubscribeList, SubscribeDetail,CertificateList,CertificateDetail,CertificateDetail


urlpatterns = [
    path('faq_categories/', Faq_categoryList.as_view(), name='faq_category_list'),
    path('faq_categories/<int:pk>/', Faq_categoryDetail.as_view(), name='faq_category_detail'),
    path('feedbacks/', FeedbackList.as_view(), name='feedback_list'),
    path('feedbacks/<int:pk>/', FeedbackDetail.as_view(), name='feedback_detail'),
    path('faqs/', FaqList.as_view(), name='faq_list'),
    path('faqs/<int:pk>/', FaqDetail.as_view(), name='faq_detail'),
    path('why_users/', WhyUsList.as_view(), name='why_user_list'),
    path('why_users/<int:pk>/', WhyUsDetail.as_view(), name='why_user_list_pk'),
    path('partners/', PartnersList.as_view(), name='partners_list'),
    path('partners/<int:pk>/', PartnersDetail.as_view(), name='partners_detail'),
    path('teams/', TeamList.as_view(), name='team_list'),
    path('teams/<int:pk>/', TeamDetail.as_view(), name='team_detail'),
    path('subscribes/', SubscribeList.as_view(), name='subscribe_list'),
    path('subscribes/<int:pk>/', SubscribeDetail.as_view(), name='subscribe_detail'),
    path('certificates/', CertificateList.as_view(), name='certificate_list'),
    path('certificates/<int:pk>/', CertificateDetail.as_view(), name='certificate_detail'),
]