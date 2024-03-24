from rest_framework.viewsets import ModelViewSet
from ..models import Card
from .serializers import CardSerializers

class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializers