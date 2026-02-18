from django.db import models
from django.conf import settings

class Product(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('approved', 'Approved'),
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    business = models.ForeignKey(
        'accounts.Business',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
