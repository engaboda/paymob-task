from rest_framework import viewsets
from .permissions import IsAuthenticatedOrCreate
from .models import PostModel
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from .serializers import PostModelSerializer, UserSerializer
# Create your views here.

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrCreate]

    def get_object(self):
        return self.request.user
    
    def get_queryset(self):
        return User.objects.all()
    
    def create(self, request, *args, **kwargs):
        email = EmailMessage('welcome', 'welcome in Wall App Three', to=[request.data.get('email')])
        email.send()
        return super().create(request, *args, **kwargs)
