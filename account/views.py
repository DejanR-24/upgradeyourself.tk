from ssl import RAND_status
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from rest_framework import viewsets, mixins,permissions, status, generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
import jwt


from .serializers import MyTokenObtainPairSerializer, UserSerializer, ClientSerializer, EmployeeSerializer, PsychologistSerializer, ClientProfileSerializer, LogoutSerializer
from .models import Client, Employee, Psychologist
from .utils import Util
from .permissions import IsClientProfileOwner

# CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

# class MyObtainTokenPairView(TokenObtainPairView):
#     permission_classes = (permissions.AllowAny,)
#     serializer_class = MyTokenObtainPairSerializer


# class RegisterView(generics.GenericAPIView):
#     queryset = Client.objects.all()
#     serializer_class= ClientSerializer
#     permission_classes=[permissions.AllowAny,]

#     def post(self, request):
#         client = request.data
#         serializer = self.serializer_class(data=client)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         client_data = serializer.data
#         client_user = User.objects.get(email=client['user']['email'])
#         token=RefreshToken.for_user(client_user).access_token
#         current_site=get_current_site(request).domain
#         relativeLink=reverse('email-verify')
#         absurl='http://'+current_site+relativeLink+"?token="+str(token)
#         email_body='Hi ' + client['user']['first_name'] + ', use link below to verify your email \n'+ absurl + '\n\n Have a good day,\n UpgradeYourself Team'
#         send_to=client['user']['email']
#         data={'email_body':email_body,'send_to':send_to,'email_subject':'Verify your email'}
#         Util.send_email(data)

#         return Response(client_data, status=status.HTTP_201_CREATED)


# class VerifyEmailView(generics.GenericAPIView):
#     queryset = Client.objects.all()
#     serializer_class= ClientSerializer

#     def get(self,request):
#         token=request.GET.get('token')
#         try:
#             payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
#             user = User.objects.get(id=payload['user_id'])
#             client = Client.objects.get(user=user)
#             if not client.is_verified:
#                 client.is_verified=True
#                 client.save()
#             return Response({'email':'Successfully activated'}, status=status.HTTP_200_OK)
#         except jwt.ExpiredSignatureError as indentifier:
#             return Response({'error':'Activation Expired'},status=status.HTTP_400_BAD_REQUEST)
#         except jwt.exceptions.DecodeError as indentifier:
#             return Response({'error':'Invalid token'},status=status.HTTP_400_BAD_REQUEST)

# class LogoutAPIView(generics.GenericAPIView):
#     serializer_class = LogoutSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self,request):

#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(status=status.HTTP_204_NO_CONTENT)

class UserViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, 
                    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
                    viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes=[permissions.AllowAny,]

    # def get_permissions(self):
    #     if self.request.method == 'GET' or 'POST' or 'PUT' or 'DELETE':
    #         self.permission_classes = (permissions.AllowAny,)
    #     return super(UserViewSet, self).get_permissions()


class ClientViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, 
                    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
                    viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = (permissions.IsAdminUser,)
        elif self.request.method == 'POST' or 'PUT' or 'DELETE':
            self.permission_classes = (permissions.AllowAny,)
        return super(ClientViewSet, self).get_permissions()

class ClientProfileViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, 
                    viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = ClientProfileSerializer
    permission_classes=[IsClientProfileOwner,]
    
    def get_queryset(self):
        return Client.objects.filter(user=self.request.user)



class EmployeeViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, 
                    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
                    viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Employee.objects.all()#.order_by('-user.date_joined')
    serializer_class = EmployeeSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'POST' or 'GET' or 'PUT' or 'DELETE':
            self.permission_classes = (permissions.IsAdminUser,)
        return super(EmployeeViewSet, self).get_permissions()

# @cache_page(CACHE_TTL)
class PsychologistViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, 
                    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
                    viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Psychologist.objects.all()
    serializer_class = PsychologistSerializer

    def get_permissions(self):
        if self.request.method == 'POST' or 'PUT' or 'DELETE':
            self.permission_classes = (permissions.IsAdminUser,)
        elif self.request.method == 'GET':
            self.permission_classes = (permissions.AllowAny,)
        return super(PsychologistViewSet, self).get_permissions()
