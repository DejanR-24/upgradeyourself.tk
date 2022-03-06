from rest_framework import routers

from .views import (
    UserViewSet,
    ClientViewSet,
    EmployeeViewSet,
    PsychologistViewSet,
    ClientProfileViewSet,
    EmployeeProfileViewSet,
    PsychologistProfileViewSet,
    UploadProfilePictureViewSet,
    PsychologistAdminViewSet,
)

router = routers.SimpleRouter()
router.register(r"users", UserViewSet)
router.register(r"clients", ClientViewSet)
router.register(r"employees", EmployeeViewSet)
router.register(r"client-profile", ClientProfileViewSet, basename="client-profile")
router.register(
    r"employee-profile",
    EmployeeProfileViewSet,
    basename="employee-profile",
)
router.register(
    r"psychologist-profile",
    PsychologistProfileViewSet,
    basename="psychologist-profile",
)
router.register(r"psychologists", PsychologistViewSet)
router.register(r"psychologists-admin", PsychologistAdminViewSet)
router.register(
    r"upload-profile-picture",
    UploadProfilePictureViewSet,
    basename="upload-profile-picture",
)
