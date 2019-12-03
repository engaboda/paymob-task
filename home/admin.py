from django.contrib import admin
from .models import PostModel
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'text', 'created_at', 'updated_at']
admin.site.register(PostModel, PostModelAdmin)