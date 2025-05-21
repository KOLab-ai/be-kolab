from django.contrib.auth.models import User
from django.db import models

from influencers.models import Category, Domicile


class Campaign(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('all', 'All'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='campaigns')
    campaign_goal = models.CharField(max_length=255)
    campaign_budget = models.CharField(max_length=100)
    campaign_timeline = models.CharField(max_length=100)
    target_socialmedia = models.JSONField(default=list)
    prefer_sosmed = models.CharField(max_length=100)
  
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    umur = models.CharField(max_length=50)

    target_location = models.ManyToManyField(Domicile, related_name='campaigns')
    target_interesting = models.ManyToManyField(Category, related_name='campaigns')

    category_product = models.CharField(max_length=100)
    description_product = models.TextField()


    def __str__(self):
        return f"{self.campaign_goal} - {self.user.fullname}"
