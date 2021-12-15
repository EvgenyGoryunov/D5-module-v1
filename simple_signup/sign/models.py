from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


# форму, с помощью которой мы будем создавать нового пользователя
class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    first_name = forms.CharField(label = "Имя")
    last_name = forms.CharField(label = "Фамилия")

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2", )