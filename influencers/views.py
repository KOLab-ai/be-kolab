from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Influencer
from .serializers import InfluencerSerializer

class InfluencerViewSet(viewsets.ModelViewSet):
    queryset = Influencer.objects.all()
    serializer_class = InfluencerSerializer
    permission_classes = [IsAuthenticated]
