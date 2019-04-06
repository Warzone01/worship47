from ckeditor.fields import RichTextField
from django.db import models
from slugger import AutoSlugField

# Create your models here.


class Registration(models.Model):
   nickname = models.CharField(max_length=30)
   email = models.CharField(max_length=100)
   password = models.CharField(max_length=100)
   confirmPassword = models.CharField(max_length=100)

   def __str__(self):
        return self.title

