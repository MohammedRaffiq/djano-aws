from django.contrib import admin

# Register your models here.
from .models import Topic,Message,Room,Profile

admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(Room)
admin.site.register(Profile)