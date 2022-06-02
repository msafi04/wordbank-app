#words/urls.py

from django.urls import path

from .views import (
    WordListView, 
    WordDetailView, 
    WordUpdateView,
    WordDeleteView,
    WordCreateView,
)

urlpatterns = [
    path('<int:pk>/edit/', WordUpdateView.as_view(), name = 'word_edit'),
    path('<int:pk>/', WordDetailView.as_view(), name = 'word_detail'),
    path('<int:pk>/delete/', WordDeleteView.as_view(), name = 'word_delete'),
    path('new/', WordCreateView.as_view(), name = 'word_new'),
    path('', WordListView.as_view(), name = 'word_list'),

]