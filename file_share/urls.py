# file_share/urls.py
from django.urls import path
from .views import register_user, share_file, download_shared_file
from .views import register_user, home


app_name = 'alam'

urlpatterns = [
    path('', register_user, name='register_user'),
    path('share/<int:user_id>/', share_file, name='share_file'),
    path('download/<int:file_id>/', download_shared_file, name='download_shared_file'),
    path('home/', home, name='home'),
]
