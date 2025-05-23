from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    ROLE_CHOICES = [
        ("marketer", "Marketer"),
        ("influencer", "Influencer"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid4)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    fullname = models.CharField(max_length=100)
    email = models.EmailField()  
    company = models.CharField(max_length=100, blank=True, null=True)
    position_title = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.fullname} - {self.role}"
