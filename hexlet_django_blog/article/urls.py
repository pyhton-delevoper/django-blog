from django.urls import path
from hexlet_django_blog.article import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:id>/', views.ArticleView.as_view(), name='show'),
    path('<str:tag>/<int:article_id>/', views.index, name='article'),
    path('create/', views.ArticleFormCreate.as_view(), name='create_form')
]