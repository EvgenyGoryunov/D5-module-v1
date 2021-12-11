from django.urls import path
from .views import PostsList, NewsDetailView, NewsCreateView, NewsUpdateView, NewsDeleteView


urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),  # Ссылка на детали новости
    path('create/', NewsCreateView.as_view(), name='news_add'),  # Ссылка на создание новости
    path('create/<int:pk>', NewsUpdateView.as_view(), name='news_update'),
    path('delete/<int:pk>', NewsDeleteView.as_view(), name='news_delete'),
]