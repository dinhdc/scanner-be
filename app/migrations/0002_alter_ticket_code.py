# Generated by Django 5.1.2 on 2024-10-18 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]