# Generated by Django 3.1.7 on 2021-03-18 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20210318_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='import_csv',
            name='lab_results_date',
            field=models.DateField(verbose_name='Lab Results Date'),
        ),
        migrations.AlterField(
            model_name='import_csv',
            name='sample_sent_date',
            field=models.DateField(verbose_name='Sample Sent Date'),
        ),
    ]
