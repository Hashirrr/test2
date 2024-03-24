from rest_framework.serializers import ModelSerializer
from ..models import Card

class CardSerializers(ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'title', 'body']