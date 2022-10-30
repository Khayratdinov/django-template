## ❗️ The project was not completed ❗️ 
**🙂 I will try to finish soon 👨🏼‍💻**

# Django Project Structure

**This is a template structure for developing django-based applications**


## change project name
```sh
python manage.py renameproject project youprojectname
```

## Generated secret key.
```sh
python manage.py generate_secret_key
```
## Save the generated secret key to `base.py` file.
```sh
python manage.py generate_secret_key -s
```


## Project Tree
```bash
.

├── deployments
├── dokcer/
│   ├── local/
│   │   ├── django/
│   │   │   └── Dockefile
│   │   └── nginx/
│   │       └── Dockerfile
│   └── production/
│       ├── django/
│       │   └── Dockefile
│       └── nginx/
│           └── Dockefile
├── docs
├── locale
├── project/
│   ├── apps/
│   │   ├── core/
│   │   │   ├── management/
│   │   │   │   └── commands/
│   │   │   │       ├── __init__.py
│   │   │   │       └── renameproject.py
│   │   │   ├── __init__.py
│   │   │   ├── migrations/
│   │   │   │   └── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── tests.py
│   │   │   └── views.py
│   │   └── __init__.py
│   ├── media
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── static
│   ├── templates
│   ├── __init__.py
│   ├── asgi.py
│   ├── urls.py
│   └── wsgi.py
├── requirements/
│   ├── base.txt
│   ├── development.txt
│   └── production.txt
├── scripts
├── .dockerignore
├── .env.example
├── .gitignore
├── docker-compose.yml
├── manage.py
└── README.md
```