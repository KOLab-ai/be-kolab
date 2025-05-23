from uuid import uuid4
from django.db import models

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Domicile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    city = models.CharField(max_length=100)

class Influencer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    full_name = models.CharField(max_length=100)
    profile_picture = models.CharField(max_length=255)
    domicile = models.ForeignKey(Domicile,on_delete=models.DO_NOTHING, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name='influencers')

    def __str__(self):
        return self.full_name

class SocialPlatform(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    influencer = models.ForeignKey(Influencer, on_delete=models.CASCADE, related_name='social_platforms')
    platform = models.CharField(max_length=50)
    profile_url = models.CharField(max_length=255)
    username = models.CharField(max_length=100)
    followers = models.PositiveIntegerField()
    engagement_rate = models.CharField(max_length=10, blank=True, null=True)
    avg_likes_per_post = models.CharField(max_length=10, blank=True, null=True)
    avg_comments_per_post = models.CharField(max_length=10, blank=True, null=True)
    avg_views_per_post = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.platform} - {self.username}"
