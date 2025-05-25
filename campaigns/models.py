import uuid
from django.contrib.auth.models import User
from django.db import models

from influencers.models import Category, Domicile, Influencer


class Campaign(models.Model):
    """
    Recommended implementation using JSONField for free-form string lists
    Use this if your database supports JSONField
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="campaigns")
    
    # Using JSONField for list data - much cleaner for free-form strings

    title = models.CharField(max_length=100, default="")  # Free-form string
    campaign_goals = models.JSONField(default=list)
    social_platforms = models.JSONField(default=list)
    budget_range = models.CharField(max_length=100)  # Free-form string
    timeline = models.CharField(max_length=100)      # Free-form string
    target_age_range = models.JSONField(default=list)
    target_gender = models.JSONField(default=list)
    preferred_platforms = models.JSONField(default=list)
    
    target_locations = models.ManyToManyField(Domicile, related_name="campaigns")
    target_interests = models.ManyToManyField(Category, related_name="campaigns")
    
    product_category = models.CharField(max_length=100)  # Free-form string
    product_description = models.TextField()
    
    recommended_influencers = models.ManyToManyField(Influencer, blank=True, related_name='recommended_for')


    def __str__(self):
        return f"{self.campaign_goals} - {self.user}"


class MatchingReport(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    influencer = models.ForeignKey(Influencer, on_delete=models.CASCADE)
    report = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("campaign", "influencer")
