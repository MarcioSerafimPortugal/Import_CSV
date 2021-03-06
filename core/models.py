from django.db import models

# Create your models here.
class Import_CSV(models.Model):
    lab_id = models.TextField(verbose_name='Lab ID')
    amostra_reference = models.CharField(verbose_name='Amostra Reference', max_length=200)
    resultado_class =  models.CharField(verbose_name='Resultado Class', max_length=75)
    results_type = models.IntegerField(verbose_name='Results Type', null=True)
    lab_name = models.CharField(verbose_name='Lab Name', max_length=75)
    subspecies = models.CharField(verbose_name='Subspecies', max_length=100)
    st = models.CharField(verbose_name='ST', max_length=50)
    foco_id_old = models.CharField(verbose_name='Foco ID Old', max_length=200)
    foco_id_new = models.CharField(verbose_name='Foco ID New', max_length=200)
    notes = models.TextField(verbose_name='Notes')
    sample_sent_date = models.TextField(verbose_name='Sample Sent Date')
    lab_results_date = models.TextField(verbose_name='Lab Results Date')






#lab_id uuid NOT NULL DEFAULT uuid_generate_v4(),
#amostra_reference character varying(200),
#resultado_class character varying(75),
#results_type integer,
#lab_name character varying(75),
#subspecies character varying(100),
#st character varying(50),
#foco_id_old character varying(200),
#foco_id_new character varying(200),
#notes text,
#sample_sent_date date,
#lab_results_date date,
