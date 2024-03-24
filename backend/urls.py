from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from myapp import views

def index(request):
    return HttpResponse('Hello')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('backend.api.urls')),
    path('', index),
    path('cards/', views.card_list, name='yes'),
]
