from django.contrib import admin
from .models import FormEntry, FilesEntry

# Register your models here.
admin.site.register(FormEntry)
admin.site.register(FilesEntry)