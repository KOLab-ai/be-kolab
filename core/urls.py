from django.contrib import admin
from django.urls import include, path, re_path

from core.views import GoogleLogin


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/auth/", include("dj_rest_auth.urls")),
    re_path(r"^api/v1/auth/accounts/", include("allauth.urls")),
    path("api/v1/auth/registration/", include("dj_rest_auth.registration.urls")),
    path("api/v1/auth/google/", GoogleLogin.as_view(), name="google_login"),
    path("api/v1/", include("influencers.urls")),
    path("api/v1/", include("profiles.urls")),
]
