# Generated by Django 4.0.4 on 2023-01-09 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_services_services_offerts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='services_offerts',
            field=models.TextField(max_length=500, null=True),
        ),
    ]