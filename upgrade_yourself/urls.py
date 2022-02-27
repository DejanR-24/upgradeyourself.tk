from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.contrib.auth import views as auth_views

from account import views as account_views
from scheduler import views as scheduler_views

router = routers.DefaultRouter()
router.register(r'users', account_views.UserViewSet) #only SuperAdmin
router.register(r'clients', account_views.ClientViewSet) #onlySuperAdmin
router.register(r'client-profile',account_views.ClientProfileViewSet,basename='client-profile') #profile-owner
router.register(r'employees', account_views.EmployeeViewSet) #superAdmin
router.register(r'employee-profile',account_views.EmployeeProfileViewSet,basename='employee-profile') #profile-owner
router.register(r'psychologists', account_views.PsychologistViewSet) 
router.register(r'psychologist-profile',account_views.PsychologistProfileViewSet,basename='psychologist-profile')
router.register(r'working-hours', scheduler_views.WorkingHoursViewSet)

router.register(r'therapy', scheduler_views.TherapyViewSet) 

router.register(r'schedule-therapy', scheduler_views.ScheduleTherapyViewSet) #client schedules therapy

router.register(r"psychologists/therapies/confirmed",scheduler_views.PsychologistsTherapiesConfirmedViewSet,basename="psychologists/therapies/confirmed")
router.register(r"psychologists/therapies/pending",scheduler_views.PsychologistsTherapiesPendingViewSet,basename="psychologists/therapies/pending")

router.register(r"psychologists/schedule",scheduler_views.ClientViewPsychologistsTherapiesViewSet,basename="psychologists/schedule")
router.register(r"client-goes-to",scheduler_views.GoesToViewSet,basename="client-goes-to")

router.register(r"psychologists-fullcalendar",scheduler_views.PsychologistsFullcalendarViewSet,basename="psychologists-fullcalendar")
router.register(r"psychologists-clients",scheduler_views.PsychologistsClientsViewSet,basename="psychologists-clients")
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

