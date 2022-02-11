from django.urls import path
from auth.views import MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenRefreshView
from auth.views import RegisterView, ClientRegisterView, EmployeeRegisterView, PsychologistRegisterView


urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('register/client/', ClientRegisterView.as_view(), name='client_auth_register'),
    path('register/employee/', EmployeeRegisterView.as_view(), name='employee_auth_register'),
    path('register/psychologist/', PsychologistRegisterView.as_view(), name='psychologist_auth_register'),
]