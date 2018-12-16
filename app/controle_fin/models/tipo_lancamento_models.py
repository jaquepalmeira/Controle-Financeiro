from django.db import models
from app.controle_fin.models.fixtures_models import StatusCadastro


CHOICES = (('1', 'Crédito',), ('2', 'Débito',), ('3', 'Despesa Fixa',))


class TipoLancamento(models.Model):
    class Meta:
        db_table = 'tipo_lancamento'
        verbose_name = 'tipo_lancamento'

    tipo_lancamento = models.CharField(max_length=100)
    is_credito_or_debito = models.CharField(choices=CHOICES, max_length=1)
    status = models.ForeignKey(StatusCadastro, on_delete=models.PROTECT)

    def __str__(self):
        return self.tipo_lancamento