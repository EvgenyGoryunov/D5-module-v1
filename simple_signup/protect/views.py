from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# создали generic-представление для отображения шаблона, унаследовав класс-представление от TemplateView
# и указав имя шаблона, так же унаследовали это представление от миксина проверки аутентификации

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # получаем весь контекст из класса-родителя
# добавили новую контекстную переменную is_not_premium, чтобы ответить на вопрос, есть ли пользователь в группе,
# мы заходим в переменную запроса self.request, из этой переменной мы можем вытащить текущего пользователя,
# в поле groups хранятся все группы, в которых он состоит, далее применяем фильтр к этим группам и ищем ту самую
# имя которой premium, после чего проверяем, есть ли какие-то значения в отфильтрованном списке, метод exists()
# вернет True, если группа premium в списке групп пользователя найдена, иначе — False,# в нашем случае нужно получить
# наоборот — True, если пользователь не находится в этой группе, поэтому добавляем отрицание not, и возвращаем контекст
        context['is_not_premium'] = not self.request.user.groups.filter(name = 'premium').exists()
        return context