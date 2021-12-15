from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),  # перенаправление корневой страницы в приложение protect
    path('', include('protect.urls')), # страница, на которую перенаправляется пользователь после успешного входа на сайт, в данном случае корневая страница сайта
    path('sign/', include('sign.urls')), # все страницы, URL которых начинается с sign/, перенаправляем в приложение sign
    path('accounts/', include('allauth.urls')), #Мы добавили перенаправление на ‘accounts/’ для всех URL, которые будут управляться подключенным пакетом.
]




