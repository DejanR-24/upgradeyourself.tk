from django.contrib.auth.models import User
from django.conf import settings
from rest_framework import viewsets, mixins,permissions, status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from djoser.views import UserViewSet


from .serializers import MyTokenObtainPairSerializer, UserSerializer, ClientSerializer, EmployeeSerializer, PsychologistSerializer
from .models import Client, Employee, Psychologist

# CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

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


# class ClientOwnerViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, 
#                     mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
#                     viewsets.GenericViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Client.objects.filter(user.id=request.user.id)
#     serializer_class = ClientSerializer

#     def get_permissions(self):
#         if self.request.method == 'GET':
#             self.permission_classes = (permissions.IsAdminUser,)
#         elif self.request.method == 'POST' or 'PUT' or 'DELETE':
#             self.permission_classes = (permissions.AllowAny,)
#         return super(ClientViewSet, self).get_permissions()


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


 
class ActivateUser(UserViewSet):
    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())
 
        # this line is the only change from the base implementation.
        kwargs['data'] = {"uid": self.kwargs['uid'], "token": self.kwargs['token']}
 
        return serializer_class(*args, **kwargs)
 
    def activation(self, request, uid, token, *args, **kwargs):
        super().activation(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)