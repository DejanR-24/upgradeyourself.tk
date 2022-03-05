from rest_framework import routers

from .views import (
    TherapyViewSet,
    WorkingHoursViewSet,
    GoesToViewSet,
    ScheduleTherapyViewSet,
    ClientViewPsychologistsFullcalendarViewSet,
    PsychologistsClientsViewSet,
    PsychologistsTherapiesPendingViewSet,
    PsychologistsTherapiesConfirmedViewSet,
)

router = routers.SimpleRouter()

router.register(r"therapy", TherapyViewSet)
router.register(r"working-hours", WorkingHoursViewSet)
router.register(r"client-goes-to", GoesToViewSet, basename="client-goes-to")
router.register(r"schedule-therapy", ScheduleTherapyViewSet)
router.register(
    r"psychologists-schedule",
    ClientViewPsychologistsFullcalendarViewSet,
    basename="psychologists-schedule",
)

router.register(
    r"psychologists-clients",
    PsychologistsClientsViewSet,
    basename="psychologists-clients",
)
router.register(
    r"psychologists/therapies/pending",
    PsychologistsTherapiesPendingViewSet,
    basename="psychologists/therapies/pending",
)
router.register(
    r"psychologists/therapies/confirmed",
    PsychologistsTherapiesConfirmedViewSet,
    basename="psychologists/therapies/confirmed",
)
