# Generated by Django 3.2 on 2023-04-04 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0004_auto_20230404_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentmodel',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
