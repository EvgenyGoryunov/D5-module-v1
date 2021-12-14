from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

urlpatterns = [

# В первых строках мы импортируем класс-представление для аутентификации LoginView
    path('login/', LoginView.as_view(template_name='sign/login.html'), name='login'),

# а заодно и для выхода из системы — Logout
# При выходе с сайта (вспоминаем кнопку, которую мы создали раньше в шаблоне index.html) Django
# перенаправит пользователя на страницу, указанную в параметре template_name класса LogoutView
    path('logout/', LogoutView.as_view(template_name='sign/logout.html'), name='logout'),
]
