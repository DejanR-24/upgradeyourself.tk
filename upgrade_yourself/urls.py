from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from account import views as account_views
from scheduler import views as scheduler_views

router = routers.DefaultRouter()
router.register(r'users', account_views.UserViewSet) #only SuperAdmin
router.register(r'clients', account_views.ClientViewSet) #onlySuperAdmin
router.register(r'employees', account_views.EmployeeViewSet) #superAdmin
router.register(r'therapy', scheduler_views.TherapyViewSet) 
router.register(r'working-hours', scheduler_views.WorkingHoursViewSet)


router.register(r'client-profile',account_views.ClientProfileViewSet,basename='client-profile') #profile-owner
router.register(r'employee-profile',account_views.EmployeeProfileViewSet,basename='employee-profile') #profile-owner
router.register(r'psychologist-profile',account_views.PsychologistProfileViewSet,basename='psychologist-profile')

router.register(r'psychologists', account_views.PsychologistViewSet)
router.register(r"client-goes-to",scheduler_views.GoesToViewSet,basename="client-goes-to")
router.register(r'schedule-therapy', scheduler_views.ScheduleTherapyViewSet) #client schedules therapy
router.register(r"psychologists-schedule",scheduler_views.ClientViewPsychologistsFullcalendarViewSet,basename="psychologists-schedule")

router.register(r"psychologists-clients",scheduler_views.PsychologistsClientsViewSet,basename="psychologists-clients")
router.register(r"psychologists/therapies/pending",scheduler_views.PsychologistsTherapiesPendingViewSet,basename="psychologists/therapies/pending")
router.register(r"psychologists/therapies/confirmed",scheduler_views.PsychologistsTherapiesConfirmedViewSet,basename="psychologists/therapies/confirmed")

router.register(r"upload-profile-picture",account_views.UploadProfilePictureViewSet,basename="upload-profile-picture")

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

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


