from django.urls import path
from .views import ProfileCreateUpdateView

urlpatterns = [
    path('profile/', ProfileCreateUpdateView.as_view(), name='profile'),
]
