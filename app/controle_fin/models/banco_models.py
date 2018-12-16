from django.db import models
from app.controle_fin.models.fixtures_models import StatusCadastro


class Banco(models.Model):
    class Meta:
        db_table = 'banco'
        verbose_name = 'banco'

    codigo = models.CharField(max_length=10)
    nome_banco = models.CharField(max_length=80)
    status = models.ForeignKey(StatusCadastro, on_delete=models.PROTECT)

    def __str__(self):
        return self.codigo + ' - ' + self.nome_banco