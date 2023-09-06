from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

<<<<<<< HEAD
from .views import LogoutView, UserRegister, UserEditApi
=======
from .views import UserRegister, UserEditApi
>>>>>>> 343ed70d07ae827d8b9bc8d279d024157b9ef0f8
urlpatterns = [
    path('register/', UserRegister.as_view()),
    path("details/<int:pk>/",UserEditApi.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
<<<<<<< HEAD
    path('logout/', LogoutView.as_view(), name='auth_logout'),

=======
>>>>>>> 343ed70d07ae827d8b9bc8d279d024157b9ef0f8
]
