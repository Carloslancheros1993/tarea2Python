# Generated by Django 2.2 on 2021-04-14 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permisos', '0007_remove_permiso_observacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='permiso',
            name='nombre',
            field=models.CharField(default='true', max_length=200),
        ),
    ]
