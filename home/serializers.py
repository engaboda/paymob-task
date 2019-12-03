from rest_framework import serializers
from .models import PostModel
from django.utils.six import text_type
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User = get_user_model()

class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ['text']

class UserSerializer(serializers.ModelSerializer):
    access = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'access']

    def get_access(self, obj):
        refresh = RefreshToken.for_user(obj)
        data = {'refresh': text_type(refresh), 'token': text_type(refresh.access_token)}
        return data    

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user