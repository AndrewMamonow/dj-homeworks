from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    context = {'object_list': Article.objects.all()}
    def get_context_data(self, **kwargs):
        article_list = []
        scope_list = []

        for article in context['object_list']:
            for scope in Tag.objects.filter(article=article).all():
                scope_list.append({'topic': scope.scope.topic, 'is_main': scope.is_main})
            article.scopes = sorted(scope_list, key=lambda x: x['is_main'], reverse=True)
            article_list.append(article)
        context['object_list'] = article_list
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
