from django.contrib import admin
from .models import story, section, Genre

# Register your models here.

@admin.register(story)
class storyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'genre', 'current_length')

@admin.register(section)
class sectionAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'story','votes', 'position', 'status')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass