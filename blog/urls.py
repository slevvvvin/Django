from django.urls import path
from .views import (HomeView, PostDetailView, AddPostView, UpdatePostView,
                    DeletePostView, AddCategoryView, CategoryView,
                    UserRegisterView, AddCommentView)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('category/<int:pk>/', CategoryView.as_view(), name='category'),
    path('post/<int:pk>/comment', AddCommentView.as_view(), name='add_comment'),
]
