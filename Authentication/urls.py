from unicodedata import name
from django.urls import path, include
from .views import *

from rest_framework import routers
router = routers.DefaultRouter()
router.register('users', UserViewSet, 'users')
app_name = 'authentication'

urlpatterns = [
    path('v1/', include(router.urls)),
    path('me/', MyInfo.as_view(), name="me")
]

