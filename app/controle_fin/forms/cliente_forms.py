from django import forms
from app.controle_fin.models.cliente_models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'