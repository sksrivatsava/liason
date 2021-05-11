from django.contrib import admin
from django.urls import path, include
from app import urls
from django.conf.urls.static import static

urlpatterns = [
    path('',include('app.urls')),
    path('admin/', admin.site.urls),
]
