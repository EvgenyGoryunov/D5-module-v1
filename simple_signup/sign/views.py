from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'


# одно view для апгрейда аккаунта до Premium - для добавления в группу premium. Для данной задачи не существует
# дженерика, а писать класс-представление для такой задачи избыточно, поэтому напишем функцию-представление.
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required


# Получили объект текущего пользователя из переменной запроса. Вытащили premium-группу из модели Group.
# Дальше проверяем, находится ли пользователь в этой группе (вдруг кто-то решил перейти по этому URL, уже имея
# Premium). И если он не в группе — добавляем. В конце перенаправляем пользователя на корневую страницу,
# используя метод redirect. Далее берем кнопку с этой функцией
@login_required
def upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name='premium')
    if not request.user.groups.filter(name='premium').exists():
        premium_group.user_set.add(user)
    return redirect('/')


# Предоставление прав пользователям
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import View
class MyView(PermissionRequiredMixin, View):
    permission_required = ('<app>.<action>_<model>',
                           '<app>.<action>_<model>')

from django.views.generic.edit import CreateView
class AddProduct(PermissionRequiredMixin, CreateView):
    permission_required = ('shop.add_product',)
        # // customize form view
# Если пользователь, который вызвал это представление относится к группе content-manager и для нее предоставлено
# это право, то представление выполнится, как и планировалось. Если же пользователь таких прав не имеет, то Django
# выбросит исключение PermissionDenied и пользователя перенаправит на страницу с ошибкой 403