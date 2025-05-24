from rest_framework import serializers

from influencers.models import Category, Domicile
from .models import Campaign


class CampaignSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Campaign
        fields = [
            "id",
            "user",
            "campaign_goal",
            "campaign_budget",
            "campaign_timeline",
            "target_socialmedia",
            "prefer_sosmed",
            "gender",
            "umur",
            "target_locations",
            "target_interests",
            "category_product",
            "description_product",
        ]

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        # Replace UUIDs with readable names
        rep["target_locations"] = [loc.city for loc in instance.target_locations.all()]
        rep["target_interests"] = [
            interest.name for interest in instance.target_interests.all()
        ]

        return rep
