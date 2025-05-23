from rest_framework import serializers

from influencers.models import Category, Domicile
from .models import Campaign

class CampaignSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Campaign
        fields = '__all__'


    def to_representation(self, instance):
        rep = super().to_representation(instance)

        # Replace UUIDs with readable names
        rep['target_locations'] = [loc.city for loc in instance.target_locations.all()]
        rep['target_interests'] = [interest.name for interest in instance.target_interests.all()]

        return rep
