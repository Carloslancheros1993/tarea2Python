# Generated by Django 2.2 on 2021-04-14 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permisos', '0002_auto_20210414_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permiso',
            name='dias',
            field=models.IntegerField(),
        ),
    ]