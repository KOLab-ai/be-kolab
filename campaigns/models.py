import uuid
from django.contrib.auth.models import User
from django.db import models
from django.utils import choices

from influencers.models import Category, Domicile


class Campaign(models.Model):
    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
    ]

    SOCIAL_MEDIA_CHOICES = [
        ("yt", "YouTube"),
        ("x", "X"),
        ("ig", "Instagram"),
        ("tiktok", "TikTok"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="campaigns")
    campaign_goal = models.CharField(max_length=255)
    campaign_budget = models.CharField(max_length=100)
    campaign_timeline = models.CharField(max_length=100)
    target_socialmedia = models.CharField(max_length=10, choices=SOCIAL_MEDIA_CHOICES)
    prefer_sosmed = models.CharField(max_length=100)

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    umur = models.CharField(max_length=50)

    target_locations = models.ManyToManyField(Domicile, related_name="campaigns")
    target_interests = models.ManyToManyField(Category, related_name="campaigns")

    category_product = models.CharField(max_length=100)
    description_product = models.TextField()

    def __str__(self):
        return f"{self.campaign_goal} - {self.user}"
