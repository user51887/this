# Generated by Django 4.0.4 on 2022-07-19 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_rename_votre_commentaire_comment_votre_nom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='votre_nom',
            field=models.CharField(max_length=50),
        ),
    ]