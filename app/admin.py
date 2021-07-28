from django.contrib import admin
from .models import CustomUser, Post
from django.contrib.auth.admin import UserAdmin 


admin.site.register(CustomUser)
admin.site.register(Post)
