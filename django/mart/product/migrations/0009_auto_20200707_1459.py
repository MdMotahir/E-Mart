# Generated by Django 2.2.1 on 2020-07-07 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20200707_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='back_image',
            field=models.ImageField(upload_to='product/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='front_image',
            field=models.ImageField(upload_to='product/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='left_image',
            field=models.ImageField(upload_to='product/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='right_image',
            field=models.ImageField(upload_to='product/'),
        ),
    ]
