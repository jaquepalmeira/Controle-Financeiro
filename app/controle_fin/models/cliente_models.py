from django.db import models
from app.controle_fin.models.fixtures_models import StatusCadastro, TipoConta
from app.controle_fin.models.pessoa_models import Pessoa
from app.controle_fin.models.agencia_models import Agencia


class Cliente(Pessoa):
    class Meta:
        db_table = 'cliente'
        verbose_name = 'cliente'

    agencia = models.ForeignKey(Agencia, on_delete=models.PROTECT)
    tipo_conta = models.ForeignKey(TipoConta, on_delete=models.PROTECT)
    numero_conta = models.CharField(max_length=10)
    dv_conta = models.CharField(max_length=2)
    status = models.ForeignKey(StatusCadastro, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome + ' / ' + self.agencia.nome_agencia + '-' + self.numero_conta