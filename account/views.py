from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.permissions import AllowAny
from rest_framework import mixins
from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import ClientSerializer, EmployeeSerializer, PsychologistSerializer, UserSerializer, RegisterSerializer
from .models import Client, Employee, Psychologist

class UserViewSet(viewsets.ModelViewSet,):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAdminUser]

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all().order_by('-date_joined')

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        def get_tokens_for_user(new_user):
            refresh = RefreshToken.for_user(new_user)
            return {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }

        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "Token": get_tokens_for_user(user),
        
        })





class ClientViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, 
                    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
                    viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Client.objects.all()#.order_by('-user.date_joined')
    serializer_class = ClientSerializer
    #permission_classes = [permissions.IsAuthenticated]
    


class EmployeeViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, 
                    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
                    viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Employee.objects.all()#.order_by('-user.date_joined')
    serializer_class = EmployeeSerializer
    #permission_classes = [permissions.IsAuthenticated]

class PsychologistViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, 
                    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
                    viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Psychologist.objects.all()#.order_by('-user.date_joined')
    serializer_class = PsychologistSerializer
    #permission_classes = [permissions.IsAuthenticated]

    search_fields = ['first_name','last_name']