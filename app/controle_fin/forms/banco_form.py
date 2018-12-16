from django import forms

from app.controle_fin.models.banco_models import Banco


class CadastroBancoForm(forms.ModelForm):
    class Meta:
        model = Banco
        fields = '__all__'