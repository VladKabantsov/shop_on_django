# Generated by Django 2.0.1 on 2018-02-14 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_product_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.DecimalField(decimal_places=2, default=555, max_digits=10),
        ),
    ]
