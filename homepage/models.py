from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class Files(models.Model):
   file = models.FileField(upload_to='documents/'),
