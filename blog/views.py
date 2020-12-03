from django.shortcuts import render, get_object_or_404
from .models import Article
from django.core.paginator import (
   Paginator, EmptyPage,
   PageNotAnInteger
)

def article_list(request):
   object_list = Article.published.all()
   paginator = Paginator(object_list, 2) # 2 articles in each page
   page = request.GET.get('page')
   try:
       articles = paginator.page(page)
   except PageNotAnInteger:
       # If page is not an integer deliver the first page
       articles = paginator.page(1)
   except EmptyPage:
       # If page is out of range deliver last page of results
       articles = paginator.page(paginator.num_pages)
   return render(request,
                 'blog/article_list.html',
                 {'page': page,
                  'articles': articles})

def article_detail(request, year, month, day, article):
    article = get_object_or_404(Article, slug=article,
                                status = 'published',
                                publish__year=year,
                                publish__month=month,
                                publish__day=day)
    return render(request,'blog/article_detail.html', {'article': article})