from django.urls import path
from . import views

urlpatterns = [
    path('', views.affiliate_list, name='affiliate_list'),
]
