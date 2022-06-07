# words/models.py

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.urls import reverse

class Word(models.Model):
    title = models.CharField('Enter Word', max_length = 255)
    body = models.TextField('Meaning')
    date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('word_detail', args = [str(self.id)])

class Book(models.Model):
    book_name = models.CharField('Book Name', max_length = 140)
    book_author = models.CharField('Author Name', max_length = 140)
    date_finished = models.CharField('Finished Reading Date', null = True, max_length = 100)
    date_created = models.DateTimeField(default = timezone.now, null = True)

    def __str__(self):
        return self.book_name
    
    def get_absolute_url(self):
        return reverse('book_detail', args = [str(self.id)])
