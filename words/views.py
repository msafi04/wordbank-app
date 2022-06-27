# words/views.py

from django.contrib.auth.mixins import LoginRequiredMixin   # for restricted access to logged in users only
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView
from django.views.generic import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from django.db.models import Q
from django.shortcuts import render
from django.core.paginator import Paginator

from itertools import chain

from .models import Word
from .models import Book

class WordListView(ListView):
    model = Word
    template_name = 'word_list.html'
    login_url = 'login'
    paginate_by = 10

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

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'book_new.html'
    fields = ('book_name', 'book_author', 'comment', 'date_finished', 'date_created')
    login_url = 'login'

    def form_valid(self, form):
        #for user authorization
        form.instance.author = self.request.user
        return super().form_valid(form)

class BookListView(ListView):
    model = Book
    template_name = 'book_all.html'
    login_url = 'login'

# multiple model listview
class MultipleModelsListView(ListView):
    model = Book
    template_name = 'book_all.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        kwargs = super(MultipleModelsListView, self).get_context_data(**kwargs)
        p = Paginator(Book.objects.select_related().all(), self.paginate_by) #to paginate custom get_context_data
        kwargs['book_objects'] = p.page(kwargs['page_obj'].number)
        return kwargs

class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'book_delete.html'
    success_url = reverse_lazy('book_all')
    login_url = 'login'

    #for restricting other users to edit/delete any articles
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if not self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'book_detail.html'
    login_url = 'login'

class SearchResultView(ListView):
    model = Word
    template_name = 'search_result.html'
    context_object_name = 'context_list'

    def get_queryset(self):
        query = self.request.GET.get('search_query')
        if query:
            object_list1 = Word.objects.filter(
                Q(title__icontains=query)
            )
            object_list2 = Book.objects.filter(
                Q(book_name__icontains=query)
            )
            context = list(chain(object_list1, object_list2))
            print(context)
            return context
        else:
            return None