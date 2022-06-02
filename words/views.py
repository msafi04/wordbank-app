# words/views.py

from django.contrib.auth.mixins import LoginRequiredMixin   # for restricted access to logged in users only
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView
from django.views.generic import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Word

class WordListView(ListView):
    model = Word
    template_name = 'word_list.html'
    login_url = 'login'

class WordDetailView(LoginRequiredMixin, DetailView):
    model = Word
    template_name = 'word_detail.html'
    login_url = 'login'

class WordUpdateView(LoginRequiredMixin, UpdateView):
    model = Word
    fields = ('title', 'body')
    template_name = 'word_edit.html'
    login_url = 'login'

    #for restricting other users to edit/delete any articles
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class WordDeleteView(LoginRequiredMixin, DeleteView):
    model = Word
    template_name = 'word_delete.html'
    success_url = reverse_lazy('word_list')
    login_url = 'login'

    #for restricting other users to edit/delete any articles
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class WordCreateView(LoginRequiredMixin, CreateView):
    model = Word
    template_name = 'word_new.html'
    fields = ('title', 'body')
    login_url = 'login'

    def form_valid(self, form):
        #for user authorization
        form.instance.author = self.request.user
        return super().form_valid(form)
