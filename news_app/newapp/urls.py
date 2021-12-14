from django.urls import path
from .views import NewsList, NewsDetailView, NewsAddView, NewsEditView, NewsDeleteView, NewsSearch, ProtectedView


urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),  # Ссылка на детали новости
    path('add/', NewsAddView.as_view(), name='news_add'),  # Ссылка на создание новости
    path('edit/<int:pk>', NewsEditView.as_view(), name='news_edit'),
    path('delete/<int:pk>', NewsDeleteView.as_view(), name='news_delete'),
    path('search/', NewsSearch.as_view(), name='news_search'),
    path('protect/', ProtectedView.as_view(), name='protected_page'),
]