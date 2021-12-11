from datetime import datetime
from django.shortcuts import render
from django.views import View  # импортируем простую вьюшку
from django.core.paginator import Paginator  # импортируем класс, позволяющий удобно осуществлять постраничный вывод
from django.views.generic import ListView
from .models import Author, Category, Post, Comment
from .filters import NewsFilter  # импортируем недавно написанный фильтр


class PostsList(ListView):
#    model = Post  # указываем модель, объекты которой мы будем выводить
#    template_name = 'posts.html'  # указываем имя шаблона, в котором будет лежать HTML,
    # в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
#    context_object_name = 'posts'  # это имя списка, в котором будут лежать все объекты, его надо указать,
    # чтобы обратиться к самому списку объектов через HTML-шаблон
#    queryset = Post.objects.order_by('-dateCreation')


    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'posts.html'  # указываем имя шаблона, в котором будет лежать HTML,
# в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'posts'  # это имя списка, в котором будут лежать все объекты, его надо указать,
# чтобы обратиться к самому списку объектов через HTML-шаблон
    ordering = ['-dateCreation']
    paginate_by = 1


    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context


'''
    def get(self, request):
        news = Post.objects.order_by('-dateCreation')
        p = Paginator(news, 1)  # создаём объект класса пагинатор, передаём ему список наших новостей и их количество для одной страницы

        news = p.get_page(request.GET.get('page', 1))  # берём номер страницы из get-запроса. Если ничего не передали, будем показывать первую страницу.
        # теперь вместо всех объектов в списке товаров хранится только нужная нам страница с товарами

        data = {
            'news': news,
        }

        return render(request, 'posts.html', data)
'''

#product_list.html







'''
# создаём представление, в котором будут детали конкретного отдельного товара
class PostsDetail(DetailView):
    model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'post.html'  # название шаблона будет product.html
    context_object_name = 'post'  # название объекта

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context['value1'] = "круто и все такое" # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу
        # другого фильтра
        return context


'''