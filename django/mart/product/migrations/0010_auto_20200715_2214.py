# Generated by Django 2.2.1 on 2020-07-15 16:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20200715_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivary_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 22, 22, 14, 25, 262875)),
        ),
    ]
