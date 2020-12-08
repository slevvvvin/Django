from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include('blog.urls')),
<<<<<<< HEAD
   path('blog', include('django.contrib.auth.urls')),
]
=======
   path('members/', include('django.contrib.auth.urls')),
   path('members/', include('members.urls')),


]
>>>>>>> fc22904904af5ea8bc2faaa7fdea0cbd2f78ec1d
