# Generated by Django 2.2.5 on 2019-10-16 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Administracion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reparaciones',
            name='clientes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administracion.Clientes'),
        ),
    ]