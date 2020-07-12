from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK)

# Create your views here.


@api_view(['GET'])
def index(request):
    return Response(
        {'message': 'Welcome to the Airbnb Host Sample API'}, HTTP_200_OK)
