from datetime import datetime
from django.shortcuts import render
from django.views import View  # импортируем простую вьюшку
from django.core.paginator import Paginator  # импортируем класс, позволяющий удобно осуществлять постраничный вывод
from django.views.generic import ListView
from .models import Author, Category, Post, Comment
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView  # импортируем необходимые дженерики

from django.forms import ModelForm, BooleanField  # Импортируем true-false поле
from .filters import NewsFilter  # импортируем написанный нами фильтр (с файла filters.py)
from .forms import NewsForm


class PostsList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'posts.html'  # указываем имя шаблона, в котором будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'posts'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    ordering = ['-dateCreation']
    paginate_by = 1

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context


# дженерик для получения деталей о товаре
class NewsDetailView(DetailView):
    template_name = 'news_detail.html'
    queryset = Post.objects.all()


# дженерик для создания объекта. Надо указать только имя шаблона и класс формы, который мы написали в прошлом юните. Остальное он сделает за вас
class NewsAddView(CreateView):
    template_name = 'news_add.html'
    form_class = NewsForm


# РАЗБРАТЬСЯ С ДАННЫМ ШАБЛОНОМ ОН ПУСТ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!????????????????
# дженерик для редактирования объекта
class NewsEditView(UpdateView):
    template_name = 'news_edit.html'
    form_class = NewsForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# РАЗБРАТЬСЯ С success_url = '/post/'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!??????????????????
# дженерик для удаления товара
class NewsDeleteView(DeleteView):
    template_name = 'news_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'  # после удаления нашей статьи нас будет перебрасывать по указанному адресу



'''



#        context['categories'] = Category.objects.all()
 #       context['form'] = NewsForm()

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса
        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый товар
            form.save()
        return super().get(request, *args, **kwargs)


        # берём значения для нового товара из POST-запроса отправленного на сервер
        author = request.POST['author']
        categoryType = request.POST['categoryType']
        category = request.POST['category']
        title = request.POST['title']
        text = request.POST['text']
        news = Post(author=author, categoryType_id=categoryType, category=category, title=title, text=text)  # создаём новый товар и сохраняем
        news.save()
        return super().get(request, *args, **kwargs)  # отправляем пользователя обратно на GET-запрос.





'''
