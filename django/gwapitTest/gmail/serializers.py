from django.contrib.auth.models import User

from social.apps.django_app.default.models import UserSocialAuth
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    googleToken = serializers.SerializerMethodField('social_auth_serializes')

    def social_auth_serializes(self, user):
        try:
            social = user.social_auth.filter(provider='google-oauth2').get()
        except:
            return None
        return social.extra_data['access_token']
    class Meta:
        model = User
        fields = ('url', 'username', 'email','googleToken')
