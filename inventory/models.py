from django.db import models


class Stock(models.Model):
    category = models.CharField(
        max_length=50, unique=True, blank=True, null=True)
    item_name = models.CharField(
        max_length=50, unique=True, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0, blank=True, null=True)
    receive_quantity = models.PositiveIntegerField(
        default=0, blank=True, null=True)
    received_by = models.CharField(max_length=50, blank=True, null=True)
    issue_quantity = models.PositiveIntegerField(
        default=0, blank=True, null=True)
    issued_by = models.CharField(max_length=50, blank=True, null=True)
    issued_to = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    reorder_level = models.PositiveIntegerField(
        default=0, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    export_to_CSV = models.BooleanField(default=False)

    def __str__(self):
        return self.item_name + " " + str(self.quantity)
