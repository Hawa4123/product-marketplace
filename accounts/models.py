from django.contrib.auth.models import AbstractUser
from django.db import models

class Business(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class User(AbstractUser):
    ROLE_CHOICES = (
        ('owner', 'Owner'),
        ('manager', 'Manager'),
        ('staff', 'Staff'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    business = models.ForeignKey(
        Business,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.username
        
