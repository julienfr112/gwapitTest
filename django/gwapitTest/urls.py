
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from gwapitTest.gmail import views
from django.conf.urls import include

#import views as localviews

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^gmail',       include(router.urls)),
    url(r'', include('rest_framework.urls', namespace='rest_framework')),
#    url(r'^admin/', admin.site.urls),
#   url(r'', include('social.apps.django_app.urls', namespace='social')),
#   url(r'^logged/',localviews.mails),
#   url(r'',        localviews.index),
]
