from unicodedata import name
from django.urls import path, include
from .views import *

app_name = 'authentication'

from rest_framework import routers
router = routers.DefaultRouter()

urlpatterns = [
    path('v1/', include(router.urls)),
    path('me/', MyInfo.as_view(), name="me")
]

