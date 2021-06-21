from django.contrib import admin
from django.db import models
from .models import Book

# Register your models here.
@admin.register(Book)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('user', 'title')
