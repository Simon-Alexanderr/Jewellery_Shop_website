# Generated by Django 5.0.1 on 2024-02-09 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_cust_tab_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='img_up',
            name='approval',
            field=models.BooleanField(default=False),
        ),
    ]
