from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class AddressTableAdmin(admin.ModelAdmin):

    list_display = ('id', 'min', 'max', 'storage_bin_address')
    list_filter = (
        'storage_bin_address',
        'id',
        'min',
        'max',
        'storage_bin_address',
    )


class ProductAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'description', 'address_table')
    list_filter = (
        'address_table',
        'id',
        'name',
        'description',
        'address_table',
    )
    search_fields = ('name',)


class StorageBinAdmin(admin.ModelAdmin):

    list_display = ('address', 'size', 'warehouse', 'type')
    list_filter = (
        'warehouse',
        'type',
        'address',
        'size',
        'warehouse',
        'type',
    )


class TypeAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'product')
    list_filter = ('product', 'id', 'name', 'product')
    search_fields = ('name',)


class WarehouseAdmin(admin.ModelAdmin):

    list_display = ('id', 'name')
    list_filter = ('id', 'name')
    search_fields = ('name',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.AddressTable, AddressTableAdmin)
_register(models.Product, ProductAdmin)
_register(models.StorageBin, StorageBinAdmin)
_register(models.Type, TypeAdmin)
_register(models.Warehouse, WarehouseAdmin)
