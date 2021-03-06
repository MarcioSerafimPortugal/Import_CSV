# Generated by Django 3.1.7 on 2021-03-17 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210306_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='import_csv',
            name='amostra_reference',
            field=models.CharField(blank=True, max_length=200, verbose_name='Amostra Reference'),
        ),
        migrations.AlterField(
            model_name='import_csv',
            name='foco_id_new',
            field=models.CharField(blank=True, max_length=200, verbose_name='Foco ID New'),
        ),
        migrations.AlterField(
            model_name='import_csv',
            name='foco_id_old',
            field=models.CharField(blank=True, max_length=200, verbose_name='Foco ID Old'),
        ),
        migrations.AlterField(
            model_name='import_csv',
            name='lab_name',
            field=models.CharField(blank=True, max_length=75, verbose_name='Lab Name'),
        ),
        migrations.AlterField(
            model_name='import_csv',
            name='lab_results_date',
            field=models.CharField(blank=True, max_length=10, verbose_name='Lab Results Date'),
        ),
        migrations.AlterField(
            model_name='import_csv',
            name='notes',
            field=models.TextField(blank=True, verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='import_csv',
            name='resultado_class',
            field=models.CharField(blank=True, max_length=75, verbose_name='Resultado Class'),
        ),
        migrations.AlterField(
            model_name='import_csv',
            name='sample_sent_date',
            field=models.CharField(blank=True, max_length=10, verbose_name='Sample Sent Date'),
        ),
        migrations.AlterField(
            model_name='import_csv',
            name='st',
            field=models.CharField(blank=True, max_length=50, verbose_name='ST'),
        ),
        migrations.AlterField(
            model_name='import_csv',
            name='subspecies',
            field=models.CharField(blank=True, max_length=100, verbose_name='Subspecies'),
        ),
    ]
