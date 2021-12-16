from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# generic-представление для отображения шаблона из папки templates, которую мы сами создали и путь до нее прописали
# в файле-настройке проекта settings.py / TEMPLATES / 'DIRS': [os.path.join(BASE_DIR, 'templates')] (+импорт модуля os),
# либо просто можно написать, 'DIRS': [BASE_DIR/'templates'], но хз, вызывало ошибку как-то раз

# данный шаблон protect/index.html запускается, если мы в приложении sign прошли аутентификацию (в соответствии
# с нашей логикой приложения),  LoginRequiredMixin - нужен для того, чтоб данный класс понял, что можно
# запускать представление, что пользователь зарегистрирован в системе
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'