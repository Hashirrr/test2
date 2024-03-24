from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CardViewSet

card_router = DefaultRouter()
card_router.register(r"cards", CardViewSet)