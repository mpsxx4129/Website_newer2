# Generated by Django 2.2.dev20180812014849 on 2019-08-09 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='My_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='special location or name')),
            ],
        ),
        migrations.DeleteModel(
            name='Datos',
        ),
        migrations.RemoveField(
            model_name='estudiantes_septimo',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Estudiantes_octavo',
        ),
        migrations.DeleteModel(
            name='Estudiantes_septimo',
        ),
    ]
