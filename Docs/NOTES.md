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
  - routings to different pages/rooms of the site.
  - so for that we can add 

```python
  path('room/<str:pk>/', views.room, name="room"),
```

  - and in the views file, where the room function is defined, pass "pk" as an argument.
  - now in the home html file add an "a" tag with the href="/room/{{room.id}}"
  now when the dynamic link is pressed, that would trigger a url and that would trigger a view,
  - currently there is no use of "pk". Later on well use the pk to query the DB.

  ```python
  def room(request, pk):
    room = None
    for i in rooms:
        if i["id"] == pk:
            room = i

    context = {"room": room}

    return render(request, 'base/room.html', context)
```

  - now u can use this context dict to access the values

## Why are we passing in a name in the url file with the path?
  - lets say in future we are about to change the url room to something else,
  - so in order for us to not change it elsewhere, we use "name"
from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) # an empty field is accespted
    # while the null field is for database, the blank is for form, the user can leave the form empty
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    # the auto_now means, whenever the table is updated, the value is updated
    # auto_now_add takse a snapshot only when it was created

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # a relationship betweeen room and message
    room = models.ForeignKey(Room, on_delete=models.CASCADE) # so if a room gets deleted, all the messages are also deleted
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
  use it in href as 
  <a href="{% url 'room' room.id %}"></a>
  - so we use an inbuilt template called url, and then pass the name and also the dynamic aspect 

# Setting up DATABASE and Admin Panel
  - so initially, django preps ready made databases to be used, they store the session ids of different users, user tables for authentication
  - but the tables are ready, yet not activated, hence the runserver gives warnings about making migrations.
  - so to execute the built in tables,
    "python manage.py migrate"
    - executes and make tables.

## Adding our own tables
  - go to the specific app and use the models.py file.
  - In order to make tables we use python classes
  - refer to {./Pasted image.png}

  - we create a room first

  ```python
  from django.db import models

class Room(models.Model):
    # host
    # topic
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) # an empty field is accespted
    # while the null field is for database, the blank is for form, the user can leave the form empty
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    # the auto_now means, whenever the table is updated, the value is updated
    # auto_now_add takse a snapshot only when it was created

    def __str__(self):
        return str(self.name)
```

  - everytime we add new tables we have to run "python manage.py makemigrations"
    - when this is done, the Django compares the tables with the old tables and then, if there are any new ones they are added
    - then migrate the database

  ## the admin Panel
    - since we have a database now, we can see the admin panel
    - go the same base url and then add /admin ta the last of it 
    - now for to access it you need to have admin level permissions.
    - to get the username and the password, set it first time
"python manage.py createsuperuser"
  - now u are eligible to enter the admin panel
  - u can add users and entries to the database.
  - but as we can see currently there is no table for the rooms, this is so because we have to add the database to the admin.py file of the app{subpart of the project}.

```python
  from django.contrib import admin
  from .models import Room

  # now register this in the admin panel
  admin.site.register(Room)
```

  - now in the admin panel, u can add the rooms manually
  
  ## getting the data from the models to the html/Frontend
  
  - now we have to get the models so that we can display them in the room and home html file
  - to get the data from models 
 
```python 
  from .models import Room 
```

  - now to use the data from the models,
  the format is as follows:
    querySet = ModelName.objects.all(), .get(), .filter(), .exclude()
      - the querySet holds the response 
      - ModelName refers to the model that we are using
      - objects is model objects attribute 
      - then we can specify what we want from the data.

  - so something like this:

```python
  def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)
```

  - NOTE - that there is a still an "id" variable, this is still printing there because
  an "id" variable is generated by default in the database,
  - now for the dynamic routing in *rooms* function
  - now u can render the data out
  -

# CRUD Operations (Create, Read, Update and Delete)

## Creating data in the database 

  - we are using the models and the with the help of pre-made forms, we will create data
  - for that
  1. create a link from home page to go to a new url
  ```html
  
  {% extends "main.html" %}
  {% block content %}
  <div>
    <form method="POST" action="">
        {% csrf_token %}
        {{form.as_p}}
        <input type="submit" value="Submit">
    </form>
  </div>
  {% endblock %}

```
  - we use the form method, to send the data to the browser
  - we use the csrf_token (cross site request forgery)

  2. make a url and view (def function)

  - url 
  ```python
  path('create-room/', views.create_room, name="create_room"),
```

  - view 
  ```python
  from .forms import RoomForm

  def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {"form":form}
    return render(request, 'base/room_form.html', context)
```
  
  - create a form variable for the RoomForm object 
  - now if the request is POST, pass the POSTED data to the RoomForm 
  - and if the form is valid, save it and redirect to the 'home' {redirect function has been imported via django.shortcuts library}

  3. now about the RoomForm
  - create a forms.py file in the base app and then import 
  ```python 
  
  from djnago.forms import ModelForm
  # and import all the models from the models file
  class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
```
  
  - this tells the django program that give the form with all the input fields that are present in the room model
  - obiously not including the date and time because they are not editable
  - now u can use the Room form
