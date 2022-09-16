
from django.contrib import admin

from .models import book

# class bookAdmin(admin.ModelAdmin):
#     list_display = ("book_name","author","category")
 

admin.site.register(book)