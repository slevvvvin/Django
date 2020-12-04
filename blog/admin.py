from django.contrib import admin
from .models import Article, Category

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'author', 'status', 'category')
    list_filter = ('status', 'created', 'author', 'category')
    search_fields = ('title', 'body', 'category')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    ordering = ['status']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)