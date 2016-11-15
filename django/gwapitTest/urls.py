
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from gwapitTest.gmail import views as googleview
from gwapitTest import views
from django.conf.urls import include

#import views as localviews

googlerouter = routers.DefaultRouter()
googlerouter.register(r'users', googleview.UserViewSet)

urlpatterns = [
    url(r'^gmail/mails', googleview.mails),
    url(r'^gmail/',      include(googlerouter.urls)),
    url(r'^auth/' ,      include('social.apps.django_app.urls', namespace='social')),
    url(r'^endpoint/(.*)', views.endpoint),
]
