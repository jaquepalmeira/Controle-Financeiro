from django.shortcuts import render, redirect, get_object_or_404

from app.controle_fin.models.lancamento_models import Lancamento


def lacamentos_faturados(request):
    lancamentos = Lancamento.objects.filter(status_lancamento=3)
    saldo = 0
    for x in lancamentos:
        if x.tipo_lancamento.tipo_lancamento == 'Debito':
            saldo -= x.valor
        elif x.tipo_lancamento.tipo_lancamento == 'Credito':
            saldo += x.valor
    return render(request, 'relatorio/lancamento_faturado.html', {'lancamentos': lancamentos, 'saldo': saldo})