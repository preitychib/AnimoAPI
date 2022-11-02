from django.urls import path
from articles import views as ArticlesViews

urlpatterns = [
    #? Articles
    path('articles/',
         ArticlesViews.ArticleListCreateAPIView.as_view(),
         name='articles-create-list'),
    path('articles/<int:pk>/',
         ArticlesViews.ArticleUpdateRetriveDeleteAPIView.as_view(),
         name='articles-retrive-update-delete'),
]