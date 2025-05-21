from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Influencer(models.Model):
    full_name = models.CharField(max_length=100)
    domicile = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name='influencers')

    def __str__(self):
        return self.full_name

class SocialPlatform(models.Model):
    influencer = models.ForeignKey(Influencer, on_delete=models.CASCADE, related_name='social_platforms')
    platform = models.CharField(max_length=50)
    profile_url = models.URLField()
    username = models.CharField(max_length=100)
    followers = models.PositiveIntegerField()
    engagement_rate = models.CharField(max_length=10, blank=True, null=True)
    avg_likes_per_post = models.CharField(max_length=10, blank=True, null=True)
    avg_comments_per_post = models.CharField(max_length=10, blank=True, null=True)
    avg_views_per_post = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.platform} - {self.username}"
