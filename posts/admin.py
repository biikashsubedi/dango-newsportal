from django.contrib import admin
from .models import *


class AdminPost(admin.ModelAdmin):
    search_fields = ['title', 'content']
    list_display = ['title', 'slug', 'date']
    list_display_links = ['title', 'slug', 'date']
    list_filter = ['date']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    list_display_links = ['title', 'slug']
    search_fields = ['title']


class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    list_display_links = ['title', 'slug']
    search_fields = ['title']


admin.site.register(Post, AdminPost)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
