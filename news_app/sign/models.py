# форма для регистрации нового пользователя, так как в джанге нет готовых решений

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# форма, с помощью которой мы будем создавать нового пользователя
# представлений реализуем Create-дженерик, расширим стандартную форму, добавив другие значимые поля:
# электронная почта; имя; фамилия нового пользователя, так как базовая форма джанги имеет только
# поле username и два поля для пароля — сам пароль и его подтверждение

class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")
    # label = "Email" - эта фраза означает, как будет именоваться данное поле на нашей форме

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2",)
