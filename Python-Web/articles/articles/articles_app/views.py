from django.urls import reverse_lazy
from django.views import generic as views

# Create your views here.
from django.views.generic.detail import SingleObjectMixin

from articles.articles_app.models import Article, Source


class ArticlesListView(views.ListView):
    template_name = 'home.html'
    model = Article


class ArticleCreateView(views.CreateView):
    template_name = 'create-article.html'
    model = Article
    fields = '__all__'
    success_url = reverse_lazy('index')


class SourcesListView(views.ListView):
    template_name = 'sources.html'
    model = Source


class SourceCreateView(views.CreateView):
    template_name = 'create-source.html'
    model = Source
    fields = '__all__'
    success_url = reverse_lazy('index')


class SourceDetailsPage(SingleObjectMixin, views.ListView):
    template_name = 'source-details.html'
    model = Source
    paginate_by = 2
    object = None

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Source.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['source'] = self.object
        return context

    def get_queryset(self):
        return self.object.article_set.all()
