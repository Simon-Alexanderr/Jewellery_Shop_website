# Generated by Django 5.0.1 on 2024-02-09 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cust_tab',
            name='address',
            field=models.CharField(max_length=200),
        ),
    ]