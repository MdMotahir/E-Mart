# Generated by Django 2.2.1 on 2020-07-15 16:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20200715_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivary_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 22, 21, 56, 15, 718827)),
        ),
    ]
