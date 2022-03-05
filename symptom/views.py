from rest_framework import mixins, viewsets, permissions

from account.permissions import IsSuperAdmin
from .models import (
    Symptom,
    PsychologicalDisorder,
    Feel,
    FieldOfExpertise,
    CharacterizedBy,
)
from .serializers import (
    SymptomSerializer,
    PsychologicalDisorderSerializer,
    FeelSerializer,
    FieldOfExpertiseSerializer,
    CharacterizedBySerializer,
)


class SymptomViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows SuperAdmin and Employees to work with symptoms.
    """
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer
    permission_classes = [IsSuperAdmin, permissions.IsAdminUser]


class PsychologicalDisorderViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows SuperAdmin and Employees to work with psychological disorders.
    """
    queryset = PsychologicalDisorder.objects.all()
    serializer_class = PsychologicalDisorderSerializer
    permission_classes = [IsSuperAdmin, permissions.IsAdminUser]


class CharacterizedByViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows SuperAdmin and Employees to work with connection between symptoms and psichological disorders.
    """
    queryset = CharacterizedBy.objects.all()
    serializer_class = CharacterizedBySerializer
    permission_classes = [IsSuperAdmin, permissions.IsAdminUser]


class FeelViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows SuperAdmin to see conection between clients and symptoms.
    """
    queryset = Feel.objects.all()
    serializer_class = FeelSerializer
    permission_classes = [IsSuperAdmin,]


class FieldOfExpertiseViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows SuperAdmin and Employees to work with conection between psychologists and symptoms.
    """
    queryset = FieldOfExpertise.objects.all()
    serializer_class = FieldOfExpertiseSerializer
    permission_classes = [IsSuperAdmin, permissions.IsAdminUser]
