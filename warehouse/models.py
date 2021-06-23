# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class AddressTable(models.Model):
    min = models.CharField(max_length=45, blank=True, null=True)
    max = models.CharField(max_length=45, blank=True, null=True)
    storage_bin_address = models.ForeignKey('StorageBin', db_column='storage_bin_address', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'address_table'

class Product(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=45, blank=True, null=True)
    address_table = models.ForeignKey(AddressTable, on_delete=models.CASCADE, blank=True, related_name='address_table')

    class Meta:
        db_table = 'product'


class StorageBin(models.Model):
    address = models.IntegerField(primary_key=True)
    size = models.CharField(max_length=45, blank=True, null=True)
    warehouse = models.ForeignKey('Warehouse', on_delete=models.CASCADE, blank=True, related_name='warehouse')
    type = models.ForeignKey('Type', db_column='Type_id', on_delete=models.CASCADE, blank=True, related_name='type')  # Field name made lowercase.

    class Meta:
        db_table = 'storage_bin'

class Type(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    product = models.ForeignKey(Product, db_column='Product_id', on_delete=models.CASCADE, blank=True, related_name='product')  # Field name made lowercase.

    class Meta:
        db_table = 'type'


class Warehouse(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'warehouse'
