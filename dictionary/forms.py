# dictionary/forms.py

from django import forms

from .models import Dictionary


class SearchForm(forms.Form):
    word = forms.CharField(max_length = 255, widget = forms.TextInput, label = 'Search Word')
