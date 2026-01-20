"""Админ-панель для приложения news."""
from django.contrib import admin
from .models import News_post

admin.site.register(News_post)
