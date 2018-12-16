from django.db import models
from app.controle_fin.models.cliente_models import Cliente
from app.controle_fin.models.tipo_lancamento_models import TipoLancamento


class StatusLancamento(models.Model):
    class Meta:
        db_table = 'status_lancamento'
        verbose_name = 'status_lancamento'
    status_lancamento = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.status_lancamento


class Lancamento(models.Model):
    class Meta:
        db_table = 'lancamento'
        verbose_name = 'lancamento'
        verbose_name_plural = 'lancamentos'

    conta_cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    descricao = models.CharField(max_length=100)
    data_lancamento = models.DateField()
    data_vencimento = models.DateField()
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    observacao = models.TextField(max_length=1000, blank=True, null=True)
    tipo_lancamento = models.ForeignKey(TipoLancamento, on_delete=models.PROTECT)
    status_lancamento = models.ForeignKey(StatusLancamento, on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao