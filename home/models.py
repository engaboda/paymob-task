from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class PostModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_post')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Post'