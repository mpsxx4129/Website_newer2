# Generated by Django 2.2.dev20180812014849 on 2018-08-23 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_datos'),
    ]

    operations = [
        migrations.AddField(
            model_name='datos',
            name='comportamiento',
            field=models.CharField(default=' STRING', max_length=30),
        ),
        migrations.AddField(
            model_name='datos',
            name='interes',
            field=models.CharField(default=' STRING', max_length=30),
        ),
        migrations.AddField(
            model_name='datos',
            name='otros',
            field=models.CharField(default=' STRING', max_length=30),
        ),
        migrations.AddField(
            model_name='datos',
            name='tardias',
            field=models.CharField(default=' STRING', max_length=30),
        ),
        migrations.AddField(
            model_name='datos',
            name='trabajos',
            field=models.CharField(default=' STRING', max_length=30),
        ),
    ]
