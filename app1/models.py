from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

from django.db import models

class Directory(models.Model):
    name = models.CharField(max_length=25)
    number = models.CharField(max_length=(10),unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    def save(self, *args, **kwarge):
    	name_number=str(self.name) + " " + str(self.number)
        self.slug=slugify(name_number)
        super(Directory,self).save(*args, **kwarge)

    def get_absolute_url(self):
        return reverse('app1:edit', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


# Create your models here.
