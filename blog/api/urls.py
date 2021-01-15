from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from blog.api import views

urlpatterns = [
    path('posts/', views.PostListAPIView.as_view()),
    path('posts/<int:pk>', views.PostDetailAPIView.as_view()),
    path('posts/create', views.PostCreateAPIView.as_view()),
    path('posts/put_delete/<int:pk>', views.PostPutDeleteAPIView.as_view()),
    path('posts/category/<int:pk>', views.PostListByCategory.as_view()),
    path('categories/', views.CategoryListAPIView.as_view()),
    path('categories/create', views.CategoryCreateAPIView.as_view()),
    path('categories/<int:pk>', views.CategoryDetailAPIView.as_view()),
    path('categories/put_delete/<int:pk>', views.CategoryPutDeleteAPIView.
         as_view()),
    path('token', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
]
