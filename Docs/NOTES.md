# What is Django?
- It is a Python Framework (collection of modules, packages, and modules)
- used for server-side development
- batteries included
- follows MVT(Model Template View) design pattern 
  - model - data access layers (database)
  - Template - Presentation layer (What the user sees)
  - View - bussiness logic

- django can be used with django rest framework to develop apis.

# Startup
- use a virtual envirnmnet (preferably uv)
- install django 
  - use uv pip install djnago
  - and django-admin as the starting command
- to start a project, 
  - use "django-admin startproject <name of the project>"
  - gives u a boilerplate for the project (gives the core config)
  - run the project with <python manage.py runserver>
  - runs the site on local host (usually port 8000)

# File Structure
- basic auto generated files are
  - asgi and wsgi files -- ## later 
  - urls file - 
    - this is the file that is used for user's redirection (contains a list of urls)
  - the main file is the settings.py file
    - it is like the command centre of the project.

# Apps in Djnago 
  - they are like the subsystem for the project 
  - for this project we have just one app.
  - to make a new app, 
    - python manage.py startapp {base}

  - now make it recognise by the project, 
    - go to settings file and in the installed app list,
    add the name as "base" or "base.apps.BaseConfig"
    check the second argument by going to base > apps > there is a function called BaseConfig.

# URL Routings and View
  - typically all the Routings are managed by the main project urls file.
  - now for a better practice, make views and urls file in the app and put the app specific urls there.
  - then route the urls from the main project to the base app

## How to do so?
  - in the main urls file.
  Add the import function from djnago.urls

```python
  from django.contrib import admin
  from django.urls import path, include

  urlpatterns = [
	  path('admin/', admin.site.urls),
	  path('', include('base.urls')),
  ]
```

  - and in the base app, add a urls file and then import the views file using 
  
```python
  from django.urls import path
  from . import views

  urlpatterns = [
	  path('', views.home, name="home"),
	  path('room/', views.rooms, name="room"),
  ]
```
```
```

  - now in the views file, u can write the functions and the logics for the pages that u want to redirect to.

```python 
  from django.shortcuts import render
  from django.http import HttpResponse

  def home(request):
	  return HttpResponse("HOME PAGE")

  def rooms(request):
	  return HttpResponse("ROOMS PAGE")
```

# Templates
- templates are text documents (generally html), that are used to define the structure and layout of the web page.
1. create a templates directory, in the main level,
2. add the room.html and home.html file.
3. let the project know of the templates dir,
  - go to settings -> templates list -> "OIRS" list and add 
  "BASE_DIR /'templates'" (try to keep it lowercase)
    - also a better way to keep the main and the nav html files in the main project
    - and the app specific html files in the base app templates as =>
    "app -> templates/{appname}/" directory,
  - now to use it, go to the views file and remove the return HTTP thing and use the imported function "return render(request, "base/home.html")"

## Template Inheritance
  - it is a way of writing a piece of code once and then using it multiple times.
  - to do so 
    - make a file and you want to get extended eg. nav.html
    - in the other files add, 
    "{% include "nav.html" %}"

 - also a u can implement something like
  - add a main file and let some part of it change with different pages.
  - create a main.html file
  - and add the usual html stuff, then in the body, specify a section as 
  "
  {% block content %}
  {% endblock content %}
  "
  - this tells the page the area where u want to add the stuff of the other pages.
  - so in a sense its just wrapping the data.
  - now to use the main files content, in the other pages as 
  "{% extends "main.html" %}"
  - and then the usual block content thing,
  write what ever u want to render in the block.

# Rendering data from views to templates

  - we usually write the logics for our page in the views file.
  - so here, we try to render out some rooms headings in the home page.

  ```python
  rooms = [
    {"id":1, "name": "Let's Learn Python"},
    {"id":2, "name": "Design WIth Me"},
    {"id":3, "name": "Frontend Developers"},
  ]
```

- now we can pass the variable in the html page in the render function of the views

```python
def home(request):
  return render(request, 'home.html',{"rooms":rooms})
```

we are passing the variable as a key value pair into the function.
- this tells that in the templates we are going to refer the rooms variableas rooms and then pass the variable in the Template.

  ### How to use it?
   - now in the home.html file.

    ```html
    {% extends "main.html" %}
    {% block content %}
      <h1>Home Template</h1>
      <div>
	      <div>
		      {% for room in rooms %}
			      <div>
				      <h5>{{room.id}} -- {{room.name}}</h5>
			      </div>
		      {% endfor %}
	      </div>
      </div>
    {% endblock content %}
  ```

  - use {{..}}  to refer to the refer to the variables.
  - And {% %}{% end %} for functions related to python.

# Dynamic Routings
  -
