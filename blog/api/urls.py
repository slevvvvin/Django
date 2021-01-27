from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from blog.api import views

router = DefaultRouter()
router.register('posts', views.PostView)
router.register('categories', views.CategoryView)

urlpatterns = [
    path('posts/category/<int:pk>', views.PostListByCategory.as_view()),
    path('token', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh', TokenRefreshView.as_view()),
    path('', include(router.urls)),
]
