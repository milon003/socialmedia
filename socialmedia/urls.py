from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),  # Include posts app URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Include authentication URLs
]