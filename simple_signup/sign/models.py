from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


# форму, с помощью которой мы будем создавать нового пользователя
class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")  # label = "Email" - эта фраза означает, что пока поле пустое, и мы еще не ввели в него свои данные, в поле будет отображаться слово "Email"
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


# импортировали класс формы, который предоставляет allauth
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group

#  В общем с приложения allauth.account.forms взяли форму SignupForm (базовая, стандартная форма), но в итоге сделаем
#  так, что при нажатии кнопки SignUp (регистрация = передача данных в базу User, то есть создание нового пользователя)
#  мы подвязывает дополнительную свою логику, которая засунет нового пользователя в нужную нам группу (базовую),
#  если просто так сохранять, то пользователь будет без группы, просто попадет в базу и все. Таким образом мы можем
#  создавать премиум группы, и создавать свои условия доступа конкретного пользователя в данную группу, например
#  оплатил подписку на месяц, а если не продлил, то алгоритм переведет его в базовую группу или иную, как укажем
class BasicSignupForm(SignupForm):
    def save(self, request):
        user = super(BasicSignupForm, self).save(request)  # вызываем этот же метод класса-родителя (save), чтобы необходимые проверки и сохранение в модель User были выполнены
        # Важно!!! Переменная basic_group (ниже), аргумент name='basic' должен соответствовать названию группы в джанге
        basic_group = Group.objects.get(name='basic')
        basic_group.user_set.add(user)  # через атрибут user_set, возвращающий список всех пользователей этой группы, мы добавляем нового пользователя в эту группу
        return user  # Обязательным требованием метода save() является возвращение объекта модели User по итогу выполнения функции
