# Generated by Django 3.1.7 on 2021-03-17 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210317_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='import_csv',
            name='results_type',
            field=models.IntegerField(blank=True, default=1, verbose_name='Results Type'),
            preserve_default=False,
        ),
    ]