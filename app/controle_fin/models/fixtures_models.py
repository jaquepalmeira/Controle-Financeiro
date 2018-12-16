from django.db import models


class StatusCadastro(models.Model):
    class Meta:
        db_table = 'status'
        verbose_name = 'status'

    status = models.CharField(max_length=25)

    def __str__(self):
        return self.status


class TipoConta(models.Model):
    class Meta:
        db_table = 'tipo_conta'
        verbose_name = 'tipo_conta'

    tipo_conta = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo_conta