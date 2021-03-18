from django.contrib import admin
from django.db import models
from import_export.admin import ImportExportModelAdmin
from core.models import Import_CSV
#from core.models import lab_results

@admin.register(Import_CSV)
# Register your models here.
class Import_CSVAdmin(ImportExportModelAdmin):
    list_display = ('amostra_reference', 'resultado_class', 'results_type', 'lab_name', 'subspecies', 'st', 'foco_id_old', 'foco_id_new', 'notes', 'sample_sent_date', 'lab_results_date')
    search_fields = ('amostra_reference', 'resultado_class', 'results_type', 'lab_name', 'subspecies', 'st', 'foco_id_old', 'foco_id_new', 'notes', 'sample_sent_date', 'lab_results_date')
    
    def custom_date(self, obj):
        return obj.sample_sent_date.strftime("%Y-%m-%d")
        return obj.lab_results_date.strftime("%Y-%m-%d") 