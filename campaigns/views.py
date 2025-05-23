from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from campaigns.methods import get_recomendations
from .models import Campaign
from .serializers import CampaignSerializer

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = [permissions.IsAuthenticated]


    @action(detail=True, methods=['get'], url_path='recommendations')
    def recommendations(self, request, pk=None):
        campaign = self.get_object()

        recommended_data = get_recomendations(campaign)

        return Response(recommended_data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Campaign.objects.filter(user=self.request.user)
