# Cursor Agent Spec (Auto) — DJ03 Django: News + Author

## Role
You are a Cursor Agent running in **Auto** mode. Follow this spec exactly.

## Goal (homework)
1. Add an `author` field to `News_post` model — a ForeignKey to Django User.
2. On `/news/` display **all fields** for each news post: title, short_description, text, pub_date, author.

## Non-negotiable constraints
- Do NOT create a new Django project.
- Do NOT rename the model `News_post`.
- Do NOT add third-party packages.
- Make minimal changes; touch only files listed below.
- Must work on Windows 11.

---

## Preflight checklist
Before editing, confirm:
1. Repository has `manage.py` in root.
2. App folder `news/` exists with `models.py`, `views.py`, `admin.py`.
3. Check `news/urls.py` — find the view function for path `''` (expected: `home`).

---

## Files to change (ONLY these)
- `news/models.py`
- `news/admin.py`
- `news/views.py`
- `news/templates/news/news.html`

A new migration file in `news/migrations/` will be created by `makemigrations`.

---

## Implementation details

### 1. `news/models.py`

#### 1.1 Add import
At the top, ensure this import exists:
```python
from django.conf import settings
```

#### 1.2 Add `author` field
Inside `class News_post(models.Model):`, add this field after existing fields:

```python
author = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    verbose_name='Автор',
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
)
```

**Why these options:**
- `settings.AUTH_USER_MODEL` — best practice (not direct User import).
- `SET_NULL` + `null=True` — avoids migration prompts for existing rows.
- `blank=True` — allows empty in admin forms.

#### 1.3 Full model example (for reference)
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

---

### 2. `news/admin.py`

Keep the simple registration from the lesson. Ensure it looks like:

```python
from django.contrib import admin
from .models import News_post

admin.site.register(News_post)
```

No additional configuration needed. The `author` field will appear in admin form automatically.

---

### 3. `news/views.py`

Edit the `home` function (or whatever function `news/urls.py` references for path `''`).

```python
from django.shortcuts import render
from .models import News_post


def home(request):
    news = News_post.objects.all()
    return render(request, 'news/news.html', {'news': news})
```

If you want to optimize (optional):
```python
news = News_post.objects.select_related('author').all()
```

---

### 4. `news/templates/news/news.html`

**Requirement:** Display ALL fields: title, short_description, text, pub_date, author.

**Important:** Keep `{% extends 'main/layoute.html' %}` — the spelling `layoute` is intentional (from the lesson project).

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

---

## Commands to run (PowerShell)
From repo root, run in order:

```powershell
python manage.py check
python manage.py makemigrations news
python manage.py migrate
python manage.py runserver
```

If any command fails — stop and fix before continuing.

---

## Acceptance criteria
1. `python manage.py runserver` starts without errors.
2. `/admin/` opens; you can create a news post and select an author.
3. `/news/` shows all news posts with ALL fields: title, short_description, text, pub_date, author.

---

## Deliverables
Modified files:
- `news/models.py`
- `news/admin.py`
- `news/views.py`
- `news/templates/news/news.html`

New file:
- `news/migrations/0002_*.py` (created by makemigrations)
