# file_sharing/urls.py
from django.contrib import admin
from django.urls import path, include
from file_share.views import register_user
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('file_share.urls')),  # Include file_share app URLs

    # Add the following line for the root path
    path('', include('file_share.urls', namespace='file_share')),
]
