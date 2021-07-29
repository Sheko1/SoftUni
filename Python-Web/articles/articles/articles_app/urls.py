from django.urls import path

from articles.articles_app.views import ArticlesListView, ArticleCreateView, SourcesListView, SourceCreateView, \
    SourceDetailsPage

urlpatterns = (
    path('', ArticlesListView.as_view(), name='index'),
    path('article/create/', ArticleCreateView.as_view(), name='create article'),
    path('sources/', SourcesListView.as_view(), name='list sources'),
    path('source/create/', SourceCreateView.as_view(), name='create source'),
    path('source/details/<int:pk>', SourceDetailsPage.as_view(), name='details source'),

)
