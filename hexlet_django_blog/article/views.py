from django.http import HttpResponse
from django.views import View


class ArticleIndex(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('article')


def index(request, tag, article_id):
    return HttpResponse(f'Статья номер {article_id} тег {tag}')