# Generated by Django 4.1.3 on 2022-11-15 17:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_data_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='data_upload',
            field=models.DateTimeField(blank=True, verbose_name=datetime.date(2022, 11, 15)),
        ),
    ]
