from django import forms
from app.controle_fin.models.lancamento_models import Lancamento


class LancamentoForm(forms.ModelForm):
    class Meta:
        model = Lancamento
        fields = '__all__'