from django.contrib import admin

# Register your models here.
from django.contrib import admin
from notes.models import Note

admin.site.register(Note)

