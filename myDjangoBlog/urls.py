from django.contrib import admin
from django.urls import path
from django.urls import include
from .yasg import urlpatterns as yasg_url


urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include('blog.urls')),
   path('', include('django.contrib.auth.urls')),
   path('api/v1/', include('blog.api.urls')),
]

urlpatterns += yasg_url
