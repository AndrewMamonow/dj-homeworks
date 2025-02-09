from django.urls import path
from debug_toolbar.toolbar import debug_toolbar_urls
from articles.views import articles_list

urlpatterns = [
    path('', articles_list, name='articles'),
    # path('__debug__/', include(debug_toolbar.urls)),
]
