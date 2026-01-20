"""Views для приложения news."""
from django.shortcuts import render
from .models import News_post


def home(request):
    """Главная страница со списком всех новостей."""
    news = News_post.objects.select_related('author').all()
    return render(request, 'news/news.html', {'news': news})
