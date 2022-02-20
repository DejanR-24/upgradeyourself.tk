from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.contrib.auth import views as auth_views

from account import views as account_views

router = routers.DefaultRouter()
router.register(r'users', account_views.UserViewSet)
router.register(r'clients', account_views.ClientViewSet)
router.register(r'employees', account_views.EmployeeViewSet)
router.register(r'psychologists', account_views.PsychologistViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register/', account_views.RegisterView.as_view(),name='register'),
    path('email_verify/', account_views.VerifyEmailView.as_view(),name='email-verify'),
    path('login/', account_views.MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
 

    path('admin/', admin.site.urls),

  
]

import debug_toolbar
urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns

