from django.conf.urls.static import static
from django.urls import path

from exam import settings
from main.views import indexview, about, contacts, service_create, service_render, login, user_login
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', indexview, name='index'),
    path('services/', service_render, name='services'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('service_add/', service_create, name='service_add'),
    path('login/', user_login, name='login'),
    path('logout/', authViews.LogoutView.as_view(next_page='index'), name='logout'),
]

