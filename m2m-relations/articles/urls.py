from django.urls import path

from articles.views import articles_list

urlpatterns = [
    path('', articles_list, name='articles'),
    path('news/', articles_list, name='articles_list'),
]
