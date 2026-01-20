# DJ03 (Django) — ДЗ: новости + автор публикации

## ✅ Статус проекта

**Проект полностью настроен и готов к использованию!**

Все требования выполнены:
- ✅ В модели `News_post` есть поле `author` (связь с пользователем Django)
- ✅ В админке можно выбрать автора при создании новости
- ✅ На `/news/` выводятся **все поля**: title, short_description, text, pub_date, author
- ✅ Все миграции применены
- ✅ Сервер запускается без ошибок

### Быстрый старт (если проект уже настроен)

```powershell
# Активация виртуального окружения
.\.venv\Scripts\Activate.ps1

# Создание суперпользователя (если ещё нет)
python manage.py createsuperuser

# Запуск сервера
python manage.py runserver
```

Затем откройте:
- Админка: http://127.0.0.1:8000/admin/
- Новости: http://127.0.0.1:8000/news/

---

## Что нужно было сделать (для справки)
**Задание из урока:**
> Создайте базу данных, в которой будут все те же поля, что мы делали на уроке, плюс поле с именем пользователя, который выкладывает новость.
> *Выводить на сайте всю информацию о новости полностью.

---

## Два варианта выполнения

### Вариант A — через Cursor Agent (рекомендуется)
1. Открой папку проекта в Cursor (где лежит `manage.py`)
2. Убедись, что в корне есть файлы:
   - `genai-readme.md`
   - `.cursorrules`
3. Открой чат с Agent (Cmd/Ctrl + L), выбери режим **Auto**
4. Вставь промпт:
   ```
   Follow genai-readme.md exactly. After edits run: python manage.py check, python manage.py makemigrations news, python manage.py migrate. Summarize changed files.
   ```
5. Проверь результат по чек-листу ниже

### Вариант B — вручную
Следуй пошаговой инструкции ниже.

---

## Пошаговая инструкция (Windows 11)

### 1. Подготовка окружения
Открой терминал в корне проекта.

**PowerShell:**
```powershell
# Создание виртуального окружения (если ещё нет)
py -m venv .venv

# Если PowerShell ругается на выполнение скриптов:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

# Активация
.\.venv\Scripts\Activate.ps1

# Установка зависимостей
pip install -r requirements.txt
```

### 2. Редактируем `news/models.py`
Добавь импорт и поле `author`:

```python
from django.db import models
from django.conf import settings


class News_post(models.Model):
    title = models.CharField('Название новости', max_length=50)
    short_description = models.CharField('Краткое описание новости', max_length=200)
    text = models.TextField('Новость')
    pub_date = models.DateTimeField('Дата публикации')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Автор',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
```

### 3. Проверяем `news/admin.py`
Должно быть:
```python
from django.contrib import admin
from .models import News_post

admin.site.register(News_post)
```

### 4. Проверяем `news/views.py`
```python
from django.shortcuts import render
from .models import News_post


def home(request):
    news = News_post.objects.all()
    return render(request, 'news/news.html', {'news': news})
```

### 5. Редактируем `news/templates/news/news.html`
```django
{% extends 'main/layoute.html' %}

{% block title %}
<title>Новостная страница</title>
{% endblock %}

{% block content %}
<h1>Новостная страница</h1>

{% for new in news %}
<div class="mb-4 p-3 border rounded">
    <h3>{{ new.title }}</h3>
    <p class="text-muted">
        {{ new.pub_date|date:"d.m.Y H:i" }} |
        Автор: {{ new.author.username|default:"—" }}
    </p>
    <p><strong>{{ new.short_description }}</strong></p>
    <div>{{ new.text|linebreaks }}</div>
</div>
{% empty %}
<p>Новостей пока нет.</p>
{% endfor %}

{% endblock %}
```

### 6. Применяем миграции
```powershell
python manage.py check
python manage.py makemigrations news
python manage.py migrate
```

### 7. Создаём суперпользователя (если ещё нет)
```powershell
python manage.py createsuperuser
```

### 8. Запускаем и проверяем
```powershell
python manage.py runserver
```

Проверки:
- `http://127.0.0.1:8000/admin/` — создай 1–2 новости, выбери автора
- `http://127.0.0.1:8000/news/` — убедись, что видны все поля

---

## Что сдавать
1. Ссылка на репозиторий GitHub
2. Два скриншота:
   - Админка: форма редактирования новости (виден выбор автора)
   - Страница `/news/`: видны все поля (title, short_description, text, pub_date, author)

---

## Частые проблемы

### PowerShell: «скрипты отключены»
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### `makemigrations` просит default для нового поля
Это решено: мы используем `null=True`, поэтому Django не спрашивает.

### WARNING: STATICFILES_DIRS directory does not exist
Создай папку, путь к которой указан в предупреждении. Не меняй settings.py наугад.

### `/news/` выдаёт 404
Проверь:
- `zerocoder/urls.py` должен содержать `path('news/', include('news.urls'))`
- `news/urls.py` должен содержать маршрут `path('', views.home, name='news_home')`

### В шаблоне ошибка «layoute not found»
Проверь, что файл `main/templates/main/layoute.html` существует. Это не опечатка — так было на уроке.
