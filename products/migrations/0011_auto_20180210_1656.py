# Generated by Django 2.0.1 on 2018-02-10 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_productimage_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.TextField(blank=True, default=None, max_length=50, null=True),
        ),
    ]