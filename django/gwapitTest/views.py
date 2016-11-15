
from django.shortcuts import render
from django.contrib.auth.models import User

def index(request):
    return render(request, 'index.html', {})

import requests
def mails(request):
    social = request.user.social_auth.filter(provider='google-oauth2').get()
    response = requests.get(
        'https://www.googleapis.com/gmail/v1/users/me/messages',
        params={'access_token': social.extra_data['access_token']}
    )
    messages = response.json()['messages']
    for message in messages[:3]:
        fullmessage=requests.get(
            'https://www.googleapis.com/gmail/v1/users/me/messages/'+message[u'id'],
            params={'access_token': social.extra_data['access_token']}
        ).json()
        message['Subject']=[kv[u'value'] for kv in fullmessage['payload']['headers'] if  kv[u'name']=='Subject'][0]
    return render(request, 'mails.html', {'messages':messages})
