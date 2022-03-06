from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from rest_framework import permissions, status, generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
import jwt

from account.serializers import ClientSerializer
from account.models import Client
from .serializers import MyTokenObtainPairSerializer, LogoutSerializer
from .utils import Util


class MyObtainTokenPairView(TokenObtainPairView):
    """
    API endpoint that allows users to login and get the tokens.
    """

    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.GenericAPIView):
    """
    API endpoint that allows clients to register and get the verification email.
    """

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [
        permissions.AllowAny,
    ]

    def post(self, request):
        client = request.data
        serializer = self.serializer_class(data=client)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        client_data = serializer.data
        client_user = User.objects.get(email=client["user"]["email"])
        token = RefreshToken.for_user(client_user).access_token
        current_site = get_current_site(request).domain
        relativeLink = reverse("email-verify")
        absurl = "http://" + current_site + relativeLink + "?token=" + str(token)
        email_body = (
            "Hi "
            + client["user"]["first_name"]
            + ", use link below to verify your email \n"
            + absurl
            + "\n\n Have a good day,\n UpgradeYourself Team"
        )
        send_to = client["user"]["email"]
        data = {
            "email_body": email_body,
            "send_to": send_to,
            "email_subject": "Verify your email",
        }
        Util.send_email(data)

        return Response(client_data, status=status.HTTP_201_CREATED)


class VerifyEmailView(generics.GenericAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get(self, request):
        token = request.GET.get("token")
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user = User.objects.get(id=payload["user_id"])
            client = Client.objects.get(user=user)
            if not client.is_verified:
                client.is_verified = True
                client.save()
            return Response(
                {"email": "Successfully activated"}, status=status.HTTP_200_OK
            )
        except jwt.ExpiredSignatureError as indentifier:
            return Response(
                {"error": "Activation Expired"}, status=status.HTTP_400_BAD_REQUEST
            )
        except jwt.exceptions.DecodeError as indentifier:
            return Response(
                {"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST
            )


class LogoutAPIView(generics.GenericAPIView):
    """
    API endpoint that allows users to logout and stores their refresh token on blacklist.
    """

    serializer_class = LogoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
