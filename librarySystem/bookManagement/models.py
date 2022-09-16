from django.db import models

# Create your models here.
from django.db import models
import uuid


class book(models.Model):
    book_id  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book_name = models.CharField(max_length=100, default='', blank=True)
    author = models.CharField(max_length=100, default='', blank=True)
    category = models.CharField(max_length=100, default='', blank=True)
    
    def __str__(self):
 
        #it will return the title
        return self.book_name


