# Generated by Django 3.1.7 on 2021-03-18 09:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_lab_resultsadmin'),
    ]

    operations = [
        migrations.DeleteModel(
            name='lab_results',
        ),
        migrations.DeleteModel(
            name='lab_resultsAdmin',
        ),
        migrations.AlterField(
            model_name='import_csv',
            name='lab_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Lab ID'),
        ),
    ]
