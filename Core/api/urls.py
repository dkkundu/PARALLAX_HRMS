from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from .views import (
    UserRegistrationView
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(),name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # UserRegistrationView
    path('signup/', UserRegistrationView.as_view(), name='signup'),



]
