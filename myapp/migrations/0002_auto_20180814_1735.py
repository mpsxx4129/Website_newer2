# Generated by Django 2.2.dev20180812014849 on 2018-08-14 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estudiante',
            options={'ordering': ['-last_name']},
        ),
        migrations.AddField(
            model_name='estudiante',
            name='assis',
            field=models.CharField(default='Ingrese si asistio', max_length=30),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='first_name',
            field=models.CharField(default='Ingrese primer nombre', max_length=30),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='last_name',
            field=models.CharField(default='Ingrese Apellidos', max_length=30),
        ),
    ]
