from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
   # post views
   path('', views.article_list, name='post_list'),
   path('<int:year>/<int:month>/<int:day>/<slug:article>/',
        views.article_detail,
        name='article_detail'),
]