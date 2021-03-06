# Generated by Django 3.0.3 on 2020-02-11 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mozi_components_datasheet', '0003_item_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('wid_name', models.CharField(max_length=200)),
                ('wid_time', models.CharField(max_length=20)),
                ('wid_quant', models.IntegerField(default=0)),
                ('wid_purp', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TransactionList1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('wid_name', models.CharField(max_length=200)),
                ('wid_time', models.CharField(max_length=20)),
                ('wid_quant', models.IntegerField(default=0)),
                ('wid_purp', models.TextField()),
            ],
        ),
    ]
