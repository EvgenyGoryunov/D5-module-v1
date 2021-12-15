from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import BaseRegisterView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='sign/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='sign/logout.html'), name='logout'),
    path('signup/', BaseRegisterView.as_view(template_name='sign/signup.html'), name='signup'),
]


# В первых строках мы импортируем класс-представление для аутентификации LoginView

# а заодно и для выхода из системы — Logout
# При выходе с сайта (кнопку, которую мы создали раньше в шаблоне index.html) Django
# перенаправит пользователя на страницу, указанную в параметре template_name класса LogoutView

# модифицировать файл конфигурации URL, чтобы Django мог увидеть представление, которое расширяет кол-во
#     полей при регистрации пользователя