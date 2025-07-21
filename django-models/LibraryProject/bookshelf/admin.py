from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns in the list view
    list_filter = ('publication_year', 'author')            # Sidebar filters
    search_fields = ('title', 'author')                     # Search box fields

