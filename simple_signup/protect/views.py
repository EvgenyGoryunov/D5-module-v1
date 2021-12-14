from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# создали generic-представление для отображения шаблона, унаследовав кастомный класс-представление от TemplateView
# и указав имя шаблона, так же унаследовали это представление от миксина проверки аутентификации
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'