from django import forms

from . import models


class ExpedienteForm(forms.ModelForm):
    class Meta:
        model = models.Expediente
        fields = "__all__"
