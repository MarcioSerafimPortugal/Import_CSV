# Generated by Django 3.1.7 on 2021-03-17 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210317_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='import_csv',
            name='lab_id',
            field=models.TextField(blank=True, verbose_name='Lab ID'),
        ),
    ]
