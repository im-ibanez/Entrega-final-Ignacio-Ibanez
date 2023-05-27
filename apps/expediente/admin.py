from django.contrib import admin

from . import models

# admin.site.register(models.ExpedienteCategorias)


@admin.register(models.Expediente)
class ExpedienteAdmin(admin.ModelAdmin):
    list_display = ("numero", "año", "caratula", "juzgado")  
    search_fields = ("numero__año",)   
    list_filter = (("numero__año", admin.RelatedOnlyFieldListFilter),)   
    ordering = ("numero",)
