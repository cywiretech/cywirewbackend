from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

@api_view(['GET'])
def getNewsletter(request):
    newsletter = Newsletter.objects.all()
    serializer = NewsletterSerial(newsletter, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def addNewsletter(request):
    serializer = NewsletterSerial(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)