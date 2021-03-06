from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from core.models import Import_CSV

@admin.register(Import_CSV)
# Register your models here.
class Import_CSVAdmin(ImportExportModelAdmin):
    list_display = ('lab_id', 'amostra_reference', 'resultado_class', 'results_type', 'lab_name', 'subspecies', 'st', 'foco_id_old', 'foco_id_new', 'notes', 'sample_sent_date', 'lab_results_date')
    pass