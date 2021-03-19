# Generated by Django 3.1.7 on 2021-03-18 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210318_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboardpanel',
            name='panel_type',
            field=models.CharField(blank=True, choices=[('barchart', 'Bar Chart'), ('piechart', 'Pie Chart'), ('table', 'Table')], default=None, max_length=127, null=True),
        ),
    ]
