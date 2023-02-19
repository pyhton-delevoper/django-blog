from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, get_object_or_404
from hexlet_django_blog.article.models import Article


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'article/index.html', context={
            'articles': articles
        })
    

class ArticleView(View):

    def get(self, request, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'article/show.html', context={
            'article': article
        })

def index(request, *args, **kwargs):
    return HttpResponse(
        f"Статья номер {kwargs['article_id']} тег {kwargs['tag']}"
    )