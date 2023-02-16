from django.contrib import admin
from .models import Article

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    
    search_fields = ['name', 'body']
    list_display = ['name', 'timestamp']
    list_filter = (('timestamp', admin.DateFieldListFilter),)