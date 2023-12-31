from django.contrib import admin
from .models import Author

# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    ordering = ['name']
