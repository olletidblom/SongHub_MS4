from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

class SubscriptionPlan(models.Model):
    """
    Represents a plan in your system: 
    Free Tier, Premium, Pro, etc.
    """
    name = models.CharField(max_length=100)
    stripe_price_id = models.CharField(max_length=100)
    storage_limit_gb = models.IntegerField(default=5)
    monthly_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

class UserSubscription(models.Model):
    """
    Links a user to a chosen subscription plan.
    Possibly store Stripe subscription IDs for reference.
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    subscription_plan = models.ForeignKey(
        SubscriptionPlan,
        on_delete=models.SET_NULL,
        null=True
    )
    stripe_subscription_id = models.CharField(
        max_length=100, null=True, blank=True
    )
    active_until = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        if self.subscription_plan:
            return f"{self.user.username} ({self.subscription_plan.name})"
        return self.user.username