# Generated by Django 3.1.7 on 2021-03-12 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_dashboardpanel'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboardpanel',
            name='dashboard_title',
            field=models.CharField(blank=True, default=None, max_length=127, null=True),
        ),
    ]
