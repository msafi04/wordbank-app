# dictionary/urls.py

from django.urls import path

from .views import DictionaryView, SearchResultView

urlpatterns = [
    #path('dictionary/', DictionaryView.as_view(), name = 'dictionary/dict_view'),
    path('dictionary/', SearchResultView.as_view(), name = 'dictionary/dict_result'),
]