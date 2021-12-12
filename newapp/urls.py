from django.urls import path
from .views import PostsList, NewsDetailView, NewsAddView, NewsEditView, NewsDeleteView, NewsSearchView


urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),  # Ссылка на детали новости
    path('add/', NewsAddView.as_view(), name='news_add'),  # Ссылка на создание новости
    path('edit/<int:pk>', NewsEditView.as_view(), name='news_edit'),
    path('delete/<int:pk>', NewsDeleteView.as_view(), name='news_delete'),
    path('search/', NewsSearchView.as_view(), name='news_search'),
]