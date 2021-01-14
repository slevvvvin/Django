from django.urls import path
from .views import (PostListAPIView, PostDetailAPIView, CategoryListAPIView,
                    CategoryDetailAPIView, PostListByCategory,
                    PostCreateAPIView, CategoryCreateAPIView,
                    PostPutDeleteAPIView, CategoryPutDeleteAPIView)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('posts/', PostListAPIView.as_view()),
    path('posts/<int:pk>', PostDetailAPIView.as_view()),
    path('posts/create', PostCreateAPIView.as_view()),
    path('posts/put_delete/<int:pk>', PostPutDeleteAPIView.as_view()),
    path('posts/category/<int:pk>', PostListByCategory.as_view()),
    path('categories/', CategoryListAPIView.as_view()),
    path('categories/create', CategoryCreateAPIView.as_view()),
    path('categories/<int:pk>', CategoryDetailAPIView.as_view()),
    path('categories/put_delete/<int:pk>', CategoryPutDeleteAPIView.as_view()),
    path('token', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
]
