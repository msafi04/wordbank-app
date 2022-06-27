# riddles/views.py

from django.contrib.auth.mixins import LoginRequiredMixin   # for restricted access to logged in users only
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView
from django.views.generic import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Riddle

from random import choice
from ast import literal_eval

import json

with open('riddles/riddles.json', 'rb') as f:
    riddle_data = json.load(f)
        
class RiddleListView(LoginRequiredMixin, ListView):
    model = Riddle
    template_name = 'riddles/riddle_list.html'
    login_url = 'login'
    
    def get_context_data(self, **kwargs):
        context = super(RiddleListView, self).get_context_data(**kwargs)
        context['my_riddle'] = choice(riddle_data)
        print(context['my_riddle'])
        return context

class RiddleAnswerView(ListView):
    model = Riddle
    template_name = 'riddles/riddle_answer.html'
    login_url = 'login'

    def get_queryset(self):
        myriddle = self.request.GET.get('myriddle')
        if myriddle:
            #context = [x for x in riddle_data if x['id'] == r_id]
            #print(literal_eval(myriddle))
            return literal_eval(myriddle)
        else:
            return None