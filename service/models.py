import os

from django.db import models


# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    preacher = models.CharField(max_length=200)
    content = models.TextField()
    location = models.CharField(max_length=200)
    attendees = models.IntegerField()

    def __str__(self):
        return self.title
