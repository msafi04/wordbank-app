# words/admin.py

from django.contrib import admin

from .models import Word
from .models import Book

admin.site.register(Word)
admin.site.register(Book)