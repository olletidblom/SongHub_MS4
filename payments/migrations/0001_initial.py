# Generated by Django 5.2 on 2025-04-09 23:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('stripe_price_id', models.CharField(max_length=100)),
                ('storage_limit_gb', models.IntegerField(default=5)),
                ('monthly_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='UserSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_subscription_id', models.CharField(blank=True, max_length=100, null=True)),
                ('active_until', models.DateTimeField(blank=True, null=True)),
                ('subscription_plan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='payments.subscriptionplan')),
            ],
        ),
    ]
