from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.contrib.auth import views as auth_views

from account import views as account_views
from scheduler import views as scheduler_views

router = routers.DefaultRouter()
router.register(r'users', account_views.UserViewSet)
router.register(r'clients', account_views.ClientViewSet)
router.register(r'client-profile',account_views.ClientProfileViewSet,basename='client-profile')
router.register(r'employees', account_views.EmployeeViewSet)
router.register(r'employee-profile',account_views.EmployeeProfileViewSet,basename='employee-profile')
router.register(r'psychologists', account_views.PsychologistViewSet)
router.register(r'psychologist-profile',account_views.PsychologistProfileViewSet,basename='psychologist-profile')
router.register(r'schedule', scheduler_views.ScheduleViewSet)
router.register(r'therapy', scheduler_views.TherapyViewSet)
router.register(r"psychologist's-therapies",scheduler_views.PsychologistsTherapiesViewSet,basename="psychologist's-therapies")

router.register(r"psychologist's-schedule",scheduler_views.ClientViewPsychologistsTherapiesViewSet,basename="psychologist's-schedule")

router.register(r"client-goes-to",scheduler_views.GoesToViewSet,basename="client-goes-to")

router.register(r"psychologist's-fullcalendar",scheduler_views.PsychologistsFullcalendarViewSet,basename="psychologist's-fullcalendar")
router.register(r"psychologist's-clients",scheduler_views.PsychologistsClientsViewSet,basename="psychologist's-clients")
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('',include('my_auth.urls')),
    path('',include('scheduler.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    path('admin/', admin.site.urls), 
]

import debug_toolbar
urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns


#in progress
urlpatterns = [
    

] + urlpatterns

