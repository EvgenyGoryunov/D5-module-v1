from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm

# представлений реализуем Create-дженерик, расширим стандартную форму, добавив другие значимые поля:
# электронная почта; имя; фамилия нового пользователя, так как базовая форма джанги имеет только
# поле username и два поля для пароля — сам пароль и его подтверждение, этого мало
class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'