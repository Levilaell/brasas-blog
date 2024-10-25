import os
from pathlib import Path
from django.db import models

BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


def caminho_imagem(instance, filename):

    date_str = instance.date.strftime('%Y/%m/%d')
    extension = filename.split('.')[-1]
    file_name = f'{date_str}.{extension}'
    
    return os.path.join(MEDIA_ROOT, file_name)


# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    preacher = models.CharField(max_length=200)
    content = models.TextField()
    location = models.CharField(max_length=200)
    attendees = models.IntegerField()
    image = models.ImageField(upload_to=caminho_imagem, null=True)

    def __str__(self):
        return self.title
