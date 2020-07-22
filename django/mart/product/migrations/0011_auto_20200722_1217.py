# Generated by Django 2.2.1 on 2020-07-22 06:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20200715_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivary_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 29, 12, 17, 49, 763463)),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
