from django import forms
from app.controle_fin.models.agencia_models import Agencia


class AgenciaForm(forms.ModelForm):
    class Meta:
        model = Agencia
        fields = '__all__'