# Generated by Django 5.0.1 on 2024-01-08 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_tenant_units'),
    ]

    operations = [
        migrations.AddField(
            model_name='units',
            name='agree_end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='units',
            name='rent_date',
            field=models.DateField(null=True),
        ),
    ]
