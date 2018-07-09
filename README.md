# Django
  
  Django is a free and open source web framework. Djangi is written in Python. A web framework is a set of components which helps to develop websites faster and easier. Django makes the process more modular to ensure easy access and modification. 
  
  When a request comes to a web server, it's passed to Django which tries to figure out what is actually requested. It takes a web page address first and tries to figure out what to do. This part is done by Django's urlresolver. Basically all the urls are contained within *urls.py*. 
  
  The functions that are associated with each url is written inside the *views.py* file. The functions are defined according to the request method **GET, POST, PUT and DELETE**. 
  
  The *models.py* contains the database tables. A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table. Each model is a Python class that subclasses **django.db.models.Model**.
  

# Installation of python and django

  Install python's latest version based on the operating system. Django supports any version of python. Django can be installed either directly using the 'pip' command or it can also be installed after creating a virtual environment. Before installing the django, it is suggested to upgrade 'pip'. 
  

Upgrade the pip using the command,
```
$ python3 -m pip install --upgrade pip
```
To install django,
```
$  python -m pip install django
```


Then create a directory and go to that directory using the command,
```
$ mkdir django_project
$ cd django_project
```

# Create django project

  The django project can be created using the following command,
```
$ C:\Users\django_project> django-admin startproject my_project
```

This command will create directories and files in the following structure,
```
django_project
├───manage.py
└───my_project
        settings.py
        urls.py
        wsgi.py
        __init__.py
```

# Create app

### Projects vs. apps
What’s the difference between a project and an app? An app is a Web application that does something – e.g., a Weblog system, a database of public records or a simple poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

To create an app, go the directory where _manage.py_ resides and type the below command,
```
$ python manage.py startapp my_app
```
The created app should be added in the **INSTALLED_APPS** in _settings.py_ in my_project.

# Routing URLs

  The URLs should be correctly routed or mapped. For that, the _urls.py_ in my_project should include the _urls.py_ in my_app.
### my_project/urls.py
```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```
# Run server

  Inorder to run the django project on the local server enter the below command on the command line,
```
$ python manage.py runserver
```
This command will run the local server by default. 

  But if you want to host the site in a specific ip address to enable access from other devices, the following command should be used,
```
$ python manage.py runserver 0.0.0.0:0000
```
Also, the allowed host in the _settings.py_ should be changed to allow other devices to access this device.
```
ALLOWED_HOSTS = ['*']
```
**NOTE: The firewall should be disabled on the device on which the site is hosted to allow other devices to access**

# Migrations

  Migrations in django are used to apply the changes made to the models into the database schema. 
- **migrate** - which is responsible for applying and unapplying migrations.
- **makemigrations** - which is responsible for creating new migrations based on the changes you have made to your models.

Commands for the above are as follows:

```
$ python manage.py migrate
$ python manage.py makemigrations
```
