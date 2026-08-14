# FocusGarden

FocusGarden is a compact Django portfolio project that turns a daily task list into a tiny digital garden. Every completed task becomes a flower; a user's daily progress is presented as a garden rather than a conventional checklist.

## Why it is a good portfolio project

- Full CRUD workflow: add, complete, and delete tasks
- Uses Django models, forms, templates, URL routing, and the admin site
- Responsive, custom visual design with no frontend framework required
- Includes clear setup instructions and clean Git hygiene

## Quick start

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

To use the Django admin:

```bash
python manage.py createsuperuser
```

Then open http://127.0.0.1:8000/admin/.

## Suggested GitHub description

> A creative Django task tracker where completed tasks bloom into a digital garden. Built with Python, Django, SQLite, HTML, and CSS.

## Resume bullet

> Built FocusGarden, a Django task-management web application that visualizes completed daily tasks as a growing garden; implemented CRUD operations, form validation, responsive UI, and SQLite persistence.
