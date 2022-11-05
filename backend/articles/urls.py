from django.urls import path
from articles.views import ArticleListView, ArticleDetailView

urlpatterns = [
    path('', ArticleListView.as_view(), name='articles'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article-detail')
]