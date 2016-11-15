
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from django.urls import reverse
from django.middleware.csrf import get_token

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def endpoint(request,provider):
    data={
        'connecturl':reverse('social:begin', kwargs={'backend': provider}),
        'disconnecturl':reverse('social:disconnect', kwargs={'backend': provider}),
        'csrf':get_token(request)
        }
    return Response(data)
