from django.urls import path

from main.views import indexview, services, about, contacts

urlpatterns = [
    path('', indexview, name='index'),
    path('services/', services, name='services'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
]
