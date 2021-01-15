from django.urls import path
from blog import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('add_category/', views.AddCategoryView.as_view(),
         name='add_category'),
    path('post/edit/<int:pk>', views.UpdatePostView.as_view(),
         name='update_post'),
    path('post/<int:pk>/delete', views.DeletePostView.as_view(),
         name='delete_post'),
    path('category/<int:pk>/', views.CategoryView.as_view(),
         name='category'),
    path('post/<int:pk>/comment', views.AddCommentView.as_view(),
         name='add_comment'),
]
