from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView, TokenObtainPairView

from .views import RegisterView, VerifyEmailView, MyObtainTokenPairView, LogoutAPIView

urlpatterns = [
    path('register/', RegisterView.as_view(),name='register'),
    path('email_verify/', VerifyEmailView.as_view(),name='email-verify'),
    #path('login/', MyObtainTokenPairView.as_view(), name='login'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]

