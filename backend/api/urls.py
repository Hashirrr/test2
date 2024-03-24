from rest_framework.routers import DefaultRouter
from myapp.api.urls import card_router
from django.urls import include, path

router = DefaultRouter()
router.registry.extend(card_router.registry)

urlpatterns = [
    path('', include(router.urls))
]
