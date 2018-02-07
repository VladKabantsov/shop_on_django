# Generated by Django 2.0.1 on 2018-02-06 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20170212_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='articul',
            field=models.CharField(blank=True, default=None, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=256, null=True),
        ),
    ]