# Generated by Django 2.2.dev20180812014849 on 2018-08-24 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_auto_20180823_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='datos',
            name='token',
            field=models.CharField(default=' STRING', max_length=200),
        ),
    ]
