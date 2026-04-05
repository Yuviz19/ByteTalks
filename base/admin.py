from django.contrib import admin
from .models import Room, Topic, Message

# now register this in the admin panel
# user model registered by default
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
