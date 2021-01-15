from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from blog.api import views

urlpatterns = [
    path('posts/', views.PostListView.as_view()),
    path('posts/<int:pk>', views.PostDetailView.as_view()),
    path('posts/new', views.PostCreateView.as_view()),
    path('posts/<int:pk>/edit', views.PostUpdateView.as_view()),
    path('posts/<int:pk>/delete', views.PostDeleteView.as_view()),
    path('posts/category/<int:pk>', views.PostListByCategory.as_view()),
    path('categories/', views.CategoryListView.as_view()),
    path('categories/new', views.CategoryCreateView.as_view()),
    path('categories/<int:pk>', views.CategoryDetailView.as_view()),
    path('categories/<int:pk>/edit', views.CategoryUpdateView.as_view()),
    path('categories/<int:pk>/delete', views.CategoryDeleteView.as_view()),
    path('token', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
]
