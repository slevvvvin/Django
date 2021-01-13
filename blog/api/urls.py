from django.urls import path
from .views import (PostListAPIView, PostDetailAPIView, CategoryListAPIView,
                    CategoryDetailAPIView, PostListByCategory)

urlpatterns = [
    path('posts/', PostListAPIView.as_view()),
    path('posts/<int:pk>', PostDetailAPIView.as_view()),
    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<int:pk>', CategoryDetailAPIView.as_view()),
    path('posts/category/<int:pk>', PostListByCategory.as_view()),
]
