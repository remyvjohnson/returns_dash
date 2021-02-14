from django.db import models

class core_return_reasons_sku(models.Model):
    ProductName = models.CharField(max_length=127)
    VariantName = models.CharField(max_length=127)
    SKU = models.CharField(max_length=127)
    ProductType = models.CharField(max_length=127)
    ProductCategory = models.CharField(max_length=127)
    ReasonID = models.IntegerField()
    Reason = models.CharField(max_length=127)
    ParentReason = models.CharField(max_length=127)
    Count = models.IntegerField()
    SalesUnits = models.IntegerField()