# форма для регистрации нового пользователя, так как в джанге нет готовых решений

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# форма, с помощью которой мы будем создавать нового пользователя
# представлений реализуем Create-дженерик, расширим стандартную форму, добавив другие значимые поля:
# электронная почта; имя; фамилия нового пользователя, так как базовая форма джанги имеет только
# поле username и два поля для пароля — сам пароль и его подтверждение

class BaseRegisterForm(UserCreationForm):
    # label = "Email" - эта фраза означает, как будет именоваться данное поле на нашей форме, слева от поля
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2")


# импортировали класс формы, который предоставляет allauth
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


#  В общем с приложения allauth.account.forms взяли форму SignupForm (базовая, стандартная форма), но в итоге сделаем
#  так, что при нажатии кнопки SignUp (регистрация = передача данных в базу User, то есть создание нового пользователя)
#  мы подвязываем дополнительную свою логику, которая внесет нового пользователя в нужную нам группу (базовую),
#  если просто так сохранять, то пользователь будет без группы, просто попадет в базу и все. Таким образом мы можем
#  создавать премиум группы, и создавать свои условия доступа конкретного пользователя в данную группу, например
#  оплатил подписку на месяц, а если не продлил, то алгоритм переведет его в базовую группу или иную, как укажем
#  Важно!!! при регистрации нового пользователя нужно обязательно выходить со всех учеток, даже с админа,
#  потом создавать нового пользователя, потом выходить и заходить уже в учетку джанги через админа и проверять
#  группу у нового пользователя
class BasicSignupForm(SignupForm):
    def save(self, request):
        # вызываем этот же метод класса-родителя (save), чтобы необходимые проверки и сохранение в модель User
        # были выполнены
        user = super(BasicSignupForm, self).save(request)
        # Важно!!! Переменная basic_group (ниже), аргумент name='basic' должен соответствовать названию группы в джанге
        basic_group = Group.objects.get(name='common')
        # через атрибут user_set, возвращающий список всех пользователей этой группы, мы добавляем нового
        # пользователя в эту группу
        basic_group.user_set.add(user)
        # Обязательным требованием метода save() является возвращение объекта модели User по итогу выполнения функции
        return user

# свои пояснения по работе верхнего алгоритма.
# мы из формы регистрации (BasicSignupForm) берем имя нового пользователя (то есть тупо шрифт,тип стринг, например
# "Vladimir"), далее находим в базе (модели Group - в ней заранее уже созданы группы), находим объект (он же наша
# группа, например "author", (находим наверное по ID группы или PK) в которую мы хотим добавить нашего пользователя,
# то есть добавить в список узеров данной группы (user_set который), тупо его логин вписываем командой add(user)
