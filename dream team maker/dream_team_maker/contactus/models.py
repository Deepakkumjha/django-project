from django.db import models

class Contact(models.Model):
    email=models.EmailField(max_length=50)
    

# Create your models here.
