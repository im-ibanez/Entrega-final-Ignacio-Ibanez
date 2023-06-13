from django.contrib import admin

from . import models

admin.site.site_title = "Expedientes"
admin.site.site_header = "Gestión de Expedientes y Evidencias"

admin.site.register(models.Evidencia)
admin.site.register(models.Juzgado)


@admin.register(models.Expediente)
class ExpedienteAdmin(admin.ModelAdmin):
    list_display = ("numero", "año", "caratula", "juzgado")  
    search_fields = ("numero__año",)   
    list_filter = (("numero__año", admin.RelatedOnlyFieldListFilter),)   
    ordering = ("numero",)


#admin.site.register(Avatar)
