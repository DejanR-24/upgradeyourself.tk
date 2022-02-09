from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from account import views as account_views
from account.views import RegisterAPI

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
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api/register/', RegisterAPI.as_view(), name='register'),

]
    
