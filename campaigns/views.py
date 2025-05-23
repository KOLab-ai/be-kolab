from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from campaigns.methods import get_recomendations, generate_report
from influencers.models import Influencer
from influencers.serializers import InfluencerSerializer
from .models import Campaign, MatchingReport
from .serializers import CampaignSerializer
from rest_framework import status


class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=["get"], url_path="matching")
    def matching(self, request, pk=None):
        campaign = self.get_object()
        influencer_id = request.query_params.get("influencerId")

        if not influencer_id:
            return Response(
                {"error": "Missing 'influencerId' query parameter."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            influencer = Influencer.objects.get(id=influencer_id)
        except Influencer.DoesNotExist:
            return Response(
                {"error": f"Influencer with id {influencer_id} not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        existing_report = MatchingReport.objects.filter(
            campaign=campaign, influencer=influencer
        ).first()

        if existing_report:
            return Response({"report": existing_report.report})

        campaign_data = CampaignSerializer(campaign).data
        influencer_data = InfluencerSerializer(influencer).data
        report = generate_report(campaign_data, influencer_data)

        MatchingReport.objects.create(
            campaign=campaign, influencer=influencer, report=report
        )

        return Response({"report": report})

    @action(detail=True, methods=["get"], url_path="recommendations")
    def recommendations(self, request, pk=None):
        campaign = self.get_object()

        recommended_data = get_recomendations(campaign)

        return Response(recommended_data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Campaign.objects.filter(user=self.request.user)
