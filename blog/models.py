from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):

    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(User, related_name='blog_categories', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Article(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='title')
    author = models.ForeignKey(User, related_name='blog_articles', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.CASCADE)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']





