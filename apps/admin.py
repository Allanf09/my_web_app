from django.contrib import admin

from .models import Post, Body, Profile


admin.site.register(Post)
admin.site.register(Body)
admin.site.register(Profile)