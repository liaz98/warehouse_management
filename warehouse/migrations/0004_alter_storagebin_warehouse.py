# Generated by Django 3.2 on 2021-06-23 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0003_auto_20210623_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storagebin',
            name='warehouse',
            field=models.ForeignKey(blank=True, default=2020.3, on_delete=django.db.models.deletion.CASCADE, to='warehouse.warehouse'),
            preserve_default=False,
        ),
    ]
