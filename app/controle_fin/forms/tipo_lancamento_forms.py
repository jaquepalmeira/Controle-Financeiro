from django import forms
from app.controle_fin.models.tipo_lancamento_models import TipoLancamento
from app.controle_fin.models.tipo_lancamento_models import CHOICES


class TipoLancamentoForm(forms.ModelForm):
    is_credito_or_debito = forms.CharField(widget=forms.RadioSelect(choices=CHOICES, attrs={'class': 'form-control-sm'}))
    class Meta:
        model = TipoLancamento
        fields = '__all__'