# Generated by Django 3.1.7 on 2021-03-18 09:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20210318_0919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='import_csv',
            name='id',
        ),
        migrations.AlterField(
            model_name='import_csv',
            name='lab_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Lab ID'),
        ),
    ]