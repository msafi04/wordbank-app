# dictionary/models.py

from django.db import models

class Dictionary(models.Model):
    word = models.CharField('Search Word', max_length = 255)

    def __unicode__(self):
        return self.word