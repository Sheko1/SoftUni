from django.contrib import admin

# Register your models here.
from articles.articles_app.models import Article, Source


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    pass
