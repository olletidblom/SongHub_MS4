from django.contrib import admin

# Register your models here.
from .models import SubscriptionPlan, UserSubscription

@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'storage_limit_gb', 'monthly_price')
    search_fields = ('name',)

@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'subscription_plan', 'stripe_subscription_id', 'active_until')
    search_fields = ('user__username', 'stripe_subscription_id')