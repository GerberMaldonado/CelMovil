# Generated by Django 2.2.5 on 2019-10-19 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Administracion', '0002_auto_20191015_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repuestos',
            name='reparaciones',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administracion.Reparaciones'),
        ),
    ]
