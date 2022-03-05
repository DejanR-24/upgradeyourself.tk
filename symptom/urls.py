from rest_framework import routers

from .views import (
    SymptomViewSet,
    PsychologicalDisorderViewSet,
    FeelViewSet,
    CharacterizedByViewSet,
    FieldOfExpertiseViewSet,
)

router = routers.SimpleRouter()
router.register(r"symptoms", SymptomViewSet)
router.register(r"psychological-disorders", PsychologicalDisorderViewSet)
router.register(r"feels", FeelViewSet)
router.register(r"characterized-by", CharacterizedByViewSet)
router.register(r"field-of-expertise", FieldOfExpertiseViewSet)
