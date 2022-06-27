#words/urls.py

from django.urls import path

from .views import (
    WordListView, 
    WordDetailView, 
    WordUpdateView,
    WordDeleteView,
    WordCreateView,
)

from .views import (
    BookCreateView, 
    BookListView, 
    MultipleModelsListView, 
    BookDeleteView,
    BookDetailView,
)

from .views import SearchResultView

urlpatterns = [
    path('<int:pk>/edit/', WordUpdateView.as_view(), name = 'word_edit'),
    path('<int:pk>/', WordDetailView.as_view(), name = 'word_detail'),
    path('<int:pk>/delete/', WordDeleteView.as_view(), name = 'word_delete'),
    path('new/', WordCreateView.as_view(), name = 'word_new'),
    path('', WordListView.as_view(), name = 'word_list'),

    path('book/<int:pk>/', BookDetailView.as_view(), name = 'book_detail'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name = 'book_delete'),
    path('book/new/', BookCreateView.as_view(), name = 'book_new'),
    path('book/', MultipleModelsListView.as_view(), name = 'book_all'),

    path('search_results/', SearchResultView.as_view(), name = 'search_result'),

]