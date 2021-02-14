# Generated by Django 3.1.6 on 2021-02-14 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='return_reasons_sku',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductName', models.CharField(max_length=127)),
                ('VariantName', models.CharField(max_length=127)),
                ('SKU', models.CharField(max_length=127)),
                ('ProductType', models.CharField(max_length=127)),
                ('ProductCategory', models.CharField(max_length=127)),
                ('ReasonID', models.IntegerField()),
                ('Reason', models.CharField(max_length=127)),
                ('ParentReason', models.CharField(max_length=127)),
                ('Count', models.IntegerField()),
                ('SalesUnits', models.IntegerField()),
            ],
        ),
    ]
