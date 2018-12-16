from django.db import models
from app.controle_fin.models.banco_models import Banco
from app.controle_fin.models.fixtures_models import StatusCadastro


class Agencia(models.Model):
    class Meta:
        db_table = 'agencia'
        verbose_name = 'agencia'

    banco = models.ForeignKey(Banco, on_delete=models.PROTECT)
    codigo_agencia = models.CharField(max_length=10)
    nome_agencia = models.CharField(max_length=80)
    status = models.ForeignKey(StatusCadastro, on_delete=models.PROTECT)

    def __str__(self):
        return self.codigo_agencia + ' - ' + self.nome_agencia