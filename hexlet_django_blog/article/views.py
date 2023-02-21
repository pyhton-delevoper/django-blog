from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from hexlet_django_blog.article.models import Article
from hexlet_django_blog.article.forms import ArticleForm
from django.contrib import messages


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


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'article/create.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'article/create.html', {'form': form})
    

class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article = Article.objects.get(id=kwargs['id'])
        form = ArticleForm(instance=article)
        return render(request, 'article/edit.html', context={
            'form': form, 'article_id': kwargs['id']
        })
    

    def post(self, request, *args, **kwargs):
        article = Article.objects.get(id=kwargs['id'])
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            message = messages.add_message(request, messages.SUCCESS, 'Success')
            return redirect('show', id=kwargs['id'])
        message = messages.add_message(request, messages.ERROR, 'Failed')
        return render(request, 'article/edit.html', context={
            'form': form, 'article_id': kwargs['id']
        })
