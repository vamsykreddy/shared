from django.db import models

# Create your models here.
class Document(models.Model):
    media = models.FileField(upload_to='')