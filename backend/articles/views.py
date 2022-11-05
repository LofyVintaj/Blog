from django .utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from articles.models import Article


class ArticleListView(ListView):

    model = Article
    template_name = "articles/list.html"
    queryset = Article.objects.order_by("-published")
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class ArticleDetailView(DetailView):

    model = Article
    template_name = "articles/detail.html"