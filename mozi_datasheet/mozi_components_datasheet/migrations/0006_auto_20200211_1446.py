# Generated by Django 3.0.3 on 2020-02-11 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mozi_components_datasheet', '0005_auto_20200211_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='not_tested',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='tested',
            field=models.IntegerField(default=0),
        ),
    ]
