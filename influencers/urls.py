from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, DomicileViewSet, InfluencerViewSet

router = DefaultRouter()
router.register(r'influencers', InfluencerViewSet, basename='influencer')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'domiciles', DomicileViewSet, basename='domiciles')

urlpatterns = [
    path('', include(router.urls)),
]
