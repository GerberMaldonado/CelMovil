# Generated by Django 2.2.5 on 2019-10-05 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Principal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Celulares',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCelulares', models.CharField(max_length=10)),
                ('codigo', models.FloatField(max_length=10)),
                ('marca', models.CharField(max_length=25)),
                ('fechaingreso', models.DateTimeField(auto_now_add=True)),
                ('serie_imei', models.DateTimeField(auto_now_add=True)),
                ('precio_mayor', models.FloatField()),
                ('precio_unidad', models.FloatField()),
            ],
        ),
    ]
