from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .api.serializers import CardSerializers  # Assuming the serializers file is in the same directory

from .models import Card  # Assuming the models file is in the parent directory

@api_view(['GET'])
def card_list(request):
    if request.method == 'GET':
        cards = Card.objects.all()  # Retrieve all Card objects from the database
        serializer = CardSerializers(cards, many=True)  # Serialize the queryset
        return Response(serializer.data, status=status.HTTP_200_OK)
