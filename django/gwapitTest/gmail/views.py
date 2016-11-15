from rest_framework import viewsets,status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.models import User
from gwapitTest.gmail.serializers import UserSerializer

from django.urls import reverse

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()#.order_by('-date_joined')
    serializer_class = UserSerializer

import requests
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def mails(request):
    social = request.user.social_auth.filter(provider='google-oauth2').get()
    response = requests.get(
        'https://www.googleapis.com/gmail/v1/users/me/messages',
        params={'access_token': social.extra_data['access_token']}
    ) #FIXME : UGLY SYNCHRONOUS REQUEST IN SERVER CODE
    if 'messages' not in response.json():
        return Response(response,status=response.status_code)
    messages = response.json()['messages']
    for message in messages[:5]:
        fullmessage=requests.get(
            'https://www.googleapis.com/gmail/v1/users/me/messages/'+message[u'id'],
            params={'access_token': social.extra_data['access_token']}
        ).json() #FIXME : UGLIER SYNCHRONOUS REQUEST IN A LOOOOOP !!!
        message['Subject']=[kv[u'value'] for kv in fullmessage['payload']['headers'] if  kv[u'name']=='Subject'][0]
    return Response({'messages':messages})
