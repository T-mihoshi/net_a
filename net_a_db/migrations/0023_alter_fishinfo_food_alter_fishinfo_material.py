# Generated by Django 4.1 on 2024-03-27 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('net_a_db', '0022_alter_fishinfo_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fishinfo',
            name='food',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='fishinfo',
            name='material',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
