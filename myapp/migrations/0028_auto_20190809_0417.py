# Generated by Django 2.2.dev20180812014849 on 2019-08-09 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_auto_20190809_0415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='download',
            name='pdf',
            field=models.FileField(upload_to='myapp/templates/download/'),
        ),
    ]
