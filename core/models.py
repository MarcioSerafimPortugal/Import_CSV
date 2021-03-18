from django.db import models
import uuid
import os

# Create your models here.
class Resultado(models.TextChoices):
        positivo = 'POSITIVO'
        negativo = 'NEGATIVO'
        rejeitava = 'REJEITADA'
        inconclusivo = 'INCONCLUSIVO'
        nao_efetuada = 'NÃO EFETUADA'
        

class Import_CSV(models.Model):
    lab_id = models.UUIDField(verbose_name='Lab ID', primary_key=True, default=uuid.uuid4, editable=False)
    amostra_reference = models.CharField(verbose_name='Amostra Reference', blank=True, max_length=200)
    resultado_class =  models.CharField(
        verbose_name='Resultado Class',
        choices= Resultado.choices,
        default= Resultado.positivo,
        max_length=75)
    results_type = models.IntegerField(verbose_name='Results Type', blank=True, null=True)
    lab_name = models.CharField(verbose_name='Lab Name', blank=True, max_length=75)
    subspecies = models.CharField(verbose_name='Subspecies', max_length=100)
    st = models.CharField(verbose_name='ST', blank=True, max_length=50)
    foco_id_old = models.CharField(verbose_name='Foco ID Old', blank=True, max_length=200)
    foco_id_new = models.CharField(verbose_name='Foco ID New', blank=True, max_length=200)
    notes = models.TextField(verbose_name='Notes', blank=True)
    sample_sent_date = models.DateField(verbose_name='Sample Sent Date')
    lab_results_date = models.DateField(verbose_name='Lab Results Date')