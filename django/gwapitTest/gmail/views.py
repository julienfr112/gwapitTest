from django.contrib.auth.models import User
#from social.storage.django_orm import DjangoUserMixin as User
from rest_framework import viewsets
from gwapitTest.gmail.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
