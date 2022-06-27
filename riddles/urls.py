# riddles/urls.py

from django.urls import path

from .views import RiddleListView, RiddleAnswerView

urlpatterns = [
        path('riddles/', RiddleListView.as_view(), name = 'riddles/riddle_list'),
        path('riddles/answer', RiddleAnswerView.as_view(), name = 'riddles/riddle_answer'),
]