# Generated by Django 3.2 on 2021-06-23 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0004_alter_storagebin_warehouse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='address_table',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='address_table', to='warehouse.addresstable'),
        ),
        migrations.AlterField(
            model_name='storagebin',
            name='type',
            field=models.ForeignKey(blank=True, db_column='Type_id', on_delete=django.db.models.deletion.CASCADE, related_name='type', to='warehouse.type'),
        ),
        migrations.AlterField(
            model_name='storagebin',
            name='warehouse',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='warehouse', to='warehouse.warehouse'),
        ),
        migrations.AlterField(
            model_name='type',
            name='product',
            field=models.ForeignKey(blank=True, db_column='Product_id', on_delete=django.db.models.deletion.CASCADE, related_name='product', to='warehouse.product'),
        ),
    ]