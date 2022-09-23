from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from rest_framework.authtoken.models import Token



class MyInfo(APIView):
    """
    API to return a static data of My personal information
    """
    permission_classes = [IsAuthenticated]
    
    def get(self, request, **kwargs):
        data = {}
        data["full_name"] = "Indra Khanal"
        data["contact"]=9846718211
        data["email"] = "indrakhanal291@gmail.com"
        data["age"] = 25
        data["experience"] = "2 year +"
        data["home_town"] = "Arjunchaupari-5, Syangja, Nepal"
        data["current_address"] = "Kathmandu"
        data["degree"] = "BScCSIT"
        data["current_position"] = "Python Developer"
        return JsonResponse({"status":status.HTTP_200_OK, "data":data})
    

    