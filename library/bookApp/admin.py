from django.contrib import admin
from bookApp.models import Book,  Comment

# Register your models here.
admin.site.register(Book)
admin.site.register(Comment)
