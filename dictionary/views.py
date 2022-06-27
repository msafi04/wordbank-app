# dictionary/views.py

from django.contrib.auth.mixins import LoginRequiredMixin   # for restricted access to logged in users only
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView
from django.views.generic import View
from django.views.generic.edit import FormView
from django.urls import reverse_lazy


from .models import Dictionary

from PyDictionary import PyDictionary

class DictionaryView(ListView):
    model = Dictionary   
    template_name = 'dictionary/dict_view.html'
    login_url = 'login'
        
class SearchResultView(LoginRequiredMixin, ListView):
    model = Dictionary
    template_name = 'dictionary/dict_result.html'
    login_url = 'login'

    def get_queryset(self):
        query = self.request.GET.get('search_query')
        if query:
            #print(query)
            dictionary = PyDictionary()
            meaning = dictionary.meaning(query)
            synonym = dictionary.synonym(query)
            antonym = dictionary.antonym(query)
            #print(meaning)
            context = {
                'word': query,
                'meaning': meaning,
                'synonym': synonym,
                'antonym': antonym
            }
            print(context)
            # to save dictionary queries to db
            #w = Dictionary(word = query)
            #w.save()
            return context
        else:
            return None