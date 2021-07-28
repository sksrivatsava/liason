from django.contrib import admin
from django.urls import path, include
from app import urls
from django.conf.urls.static import static

urlpatterns = [
    path('',include('app.urls')),
    path('admin/', admin.site.urls),
    
url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)