# Django News Board — DJ03 Homework | Домашнее задание DJ03

> **Статус проекта / Project Status:** ✅ Проект полностью настроен и готов к использованию. Все миграции применены, модель `News_post` содержит поле `author`.  
> ✅ Project is fully configured and ready to use. All migrations applied, `News_post` model contains `author` field.

---

## Features | Возможности

- **News_post model** with fields:
  - `title` — news title
  - `short_description` — brief description
  - `text` — full article text
  - `pub_date` — publication date
  - `author` — link to Django User (publisher)

- **Модель News_post** с полями:
  - `title` — название новости
  - `short_description` — краткое описание
  - `text` — полный текст новости
  - `pub_date` — дата публикации
  - `author` — связь с пользователем Django (автор публикации)

- **Admin panel** — create and manage news posts with author selection  
  **Админ-панель** — создание и управление новостями с выбором автора

- **News page** (`/news/`) — displays all news posts with complete information  
  **Страница новостей** (`/news/`) — отображает все новости с полной информацией

---

## Tech Stack | Технологии

- Python 3.x
- Django 5.x
- SQLite (default `db.sqlite3`)
- Django Templates
- Bootstrap (via base template)

---

## Quick Start | Быстрый старт (Windows 11)

### 1. Clone and setup environment | Клонирование и настройка окружения

```powershell
git clone <repository-url>
cd <repository-folder>

py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. Run migrations | Применение миграций

```powershell
python manage.py migrate
```

### 3. Create admin user | Создание администратора

```powershell
python manage.py createsuperuser
```

### 4. Start development server | Запуск сервера разработки

```powershell
python manage.py runserver
```

### 5. Access the application | Доступ к приложению

- Admin panel: <http://127.0.0.1:8000/admin/>  
  Админ-панель: <http://127.0.0.1:8000/admin/>

- News page: <http://127.0.0.1:8000/news/>  
  Страница новостей: <http://127.0.0.1:8000/news/>

---

## Project Structure | Структура проекта

```text
zerocoder/          # Django project settings
├── settings.py
├── urls.py
└── ...

main/               # Main app (base templates, home page)
├── templates/
│   └── main/
│       └── layoute.html    # Base template
└── ...

news/               # News app
├── migrations/
├── templates/
│   └── news/
│       └── news.html       # News list template
├── models.py               # News_post model
├── views.py                # home view
├── admin.py                # Admin registration
└── urls.py                 # URL routing
```

---

## Screenshots | Скриншоты

| Admin Panel                                | News Page             |
|--------------------------------------------|-----------------------|
| Create/edit news with author               | All fields displayed  |
| Создание/редактирование новостей с автором | Отображаются все поля |

---

## Course Info | Информация о курсе

**Course / Курс:** Python Developer with ChatGPT 2.0  
**Topic / Тема:** Web Development with Django  
**Lesson / Урок:** DJ03 — Creating Applications and Working with Models

---

## License | Лицензия

Educational project.  
Образовательный проект.
