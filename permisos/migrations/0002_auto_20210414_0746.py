# Generated by Django 2.2 on 2021-04-14 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permisos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permiso',
            name='dias',
            field=models.IntegerField(max_length=30),
        ),
    ]
