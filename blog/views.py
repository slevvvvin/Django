from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Article, Category
from django.core.paginator import (
   Paginator, EmptyPage,
   PageNotAnInteger
)

class ArticleList(generic.ListView):
   queryset = Article.objects.filter(status='published').order_by('-created')
   template_name = 'index.html'


class ArticleDetail(generic.DetailView):
   model = Article
   template_name = 'article_detail.html'