from django import forms

from . import models


class ExpedienteForm(forms.ModelForm):
    class Meta:
        model = models.Expediente
        fields = "__all__"

class JuzgadoForm(forms.ModelForm):
    class Meta:
        model = models.Juzgado
        fields = "__all__"

class EvidenciaForm(forms.ModelForm):
    class Meta:
        model = models.Evidencia
        fields = "__all__"
