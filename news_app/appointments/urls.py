from django.urls import path, include
from .views import AppointmentView


urlpatterns = [

    # модуль Д6 - отправка писем
    path('', AppointmentView.as_view()),
]