from django.urls import path, include
from .views import AppointmentView


urlpatterns = [

    # модуль Д6 - отправка писем
    # http://127.0.0.1:8000/appointment/
    path('', AppointmentView.as_view(), name='make_appointment'),
    path('/appointments:make_appointment/', AppointmentView.as_view()),
    # path('', AppointmentView.as_view()),

]