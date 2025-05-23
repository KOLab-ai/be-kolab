from rest_framework import viewsets
from rest_framework.pagination import BasePagination
from rest_framework.permissions import IsAuthenticated
from .models import Category, Domicile, Influencer
from .serializers import CategorySerializer, DomicileSerializer, InfluencerSerializer

class InfluencerViewSet(viewsets.ModelViewSet):
    queryset = Influencer.objects.all()
    serializer_class = InfluencerSerializer
    permission_classes = [IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

class DomicileViewSet(viewsets.ModelViewSet):
    queryset = Domicile.objects.all()
    serializer_class = DomicileSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None
