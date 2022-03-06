from rest_framework import routers

from .views import (
    SymptomViewSet,
    PsychologicalDisorderViewSet,
    FeelViewSet,
    FeelAdminViewSet,
    FeelPsychologistsViewSet,
    CharacterizedByViewSet,
    FieldOfExpertiseViewSet,
    FieldOfExpertiseAdminViewSet,
)

router = routers.SimpleRouter()
router.register(r"symptoms", SymptomViewSet)
router.register(r"psychological-disorders", PsychologicalDisorderViewSet)
router.register(r"feels", FeelViewSet, basename="feels")
router.register(r"client-feels", FeelPsychologistsViewSet, basename="client-feels")
router.register(r"feels-admin", FeelAdminViewSet, basename="feels-admin")
router.register(r"characterized-by", CharacterizedByViewSet)
router.register(
    r"field-of-expertise", FieldOfExpertiseViewSet, basename="field-of-expertise"
)
router.register(
    r"field-of-expertise-admin",
    FieldOfExpertiseAdminViewSet,
    basename="field-of-expertise-admin",
)
