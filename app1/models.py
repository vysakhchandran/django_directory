from __future__ import unicode_literals

from django.db import models

class Directory(models.Model):
    name = models.CharField(max_length=25)

    number = models.CharField(max_length=(10),unique=True)
    def __str__(self):

        return self.name

# Create your models here.
