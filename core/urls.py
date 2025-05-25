from django.contrib import admin
from django.urls import include, path, re_path

from rest_framework_simplejwt.views import  TokenRefreshView
from core.views import GoogleLogin, LoginAPIView, RegisterView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/auth/", include("dj_rest_auth.urls")),
    re_path(r"^api/v1/auth/accounts/", include("allauth.urls")),
    path("api/v1/auth/registration/", include("dj_rest_auth.registration.urls")),
    path("api/v1/auth/google/", GoogleLogin.as_view(), name="google_login"),
    path("api/v1/", include("influencers.urls")),
    path("api/v1/", include("profiles.urls")),
    path("api/v1/", include("campaigns.urls")),
    path("api/v1/login/", LoginAPIView.as_view(), name="login"),
    path("api/v1/login/refresh/", TokenRefreshView.as_view(), name="login_refresh"),
    path('api/v1/register/', RegisterView.as_view(), name='register'),
]

