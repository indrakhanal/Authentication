from djoser.serializers import UserCreateSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from rest_framework_simplejwt.utils import datetime_from_epoch

User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'password')


class TokenObtainSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        refresh_token = RefreshToken.for_user(user)
        jti = refresh_token[api_settings.JTI_CLAIM]
        exp = refresh_token['exp']
        OutstandingToken.objects.create(
                user=user,
                jti=jti,
                token=str(refresh_token),
                created_at=refresh_token.current_time,
                expires_at=datetime_from_epoch(exp),
            )
        return refresh_token

    def validate(self, attrs):

        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        return data


class CustomObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainSerializer