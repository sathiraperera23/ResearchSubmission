from django.db import models
# Create your models here.


class Files(models.Model):
    file = models.FileField(upload_to='documents/'),


class FileData(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    file = models.FileField()
