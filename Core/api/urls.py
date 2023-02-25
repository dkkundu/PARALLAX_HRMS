from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from .views import (
    UserRegistrationView, UserProfileView, LogoutView
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # Registration View
    path('signup/', UserRegistrationView.as_view(), name='signup'),
    path('profile/', UserProfileView.as_view(), name='profile_update'),

]
