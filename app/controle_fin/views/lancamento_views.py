from datetime import date, datetime
from django.shortcuts import render, redirect, get_object_or_404
from app.controle_fin.forms.lancamento_forms import LancamentoForm
from app.controle_fin.models.lancamento_models import Lancamento, \
    StatusLancamento
from app.controle_fin.utils.utils import paginattion_create



def cadastrar_lancamento(request):
    if request.method == 'POST':
        form = LancamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('controle_fin:cadastrar_lancamento')
    else:
        form = LancamentoForm()
        return render(request, 'lacamento/cadastrar_lancamento.html', {'form': form})


def editar_lancamento(request, pk):
    lancamento = get_object_or_404(Lancamento, pk=pk)
    if request.method == 'POST':
        form = LancamentoForm(request.POST, instance=lancamento)
        if form.is_valid():
            form.save()
            return redirect('controle_fin:pesquisar_lancamento')
    else:
        form = LancamentoForm(instance=lancamento)
        return render(request, 'lacamento/editar_lancamento.html', {'form': form})


def excluir_lancamento(request, pk):
    lancamento = get_object_or_404(Lancamento, pk=pk)
    lancamento.delete()
    return redirect('controle_fin:pesquisar_lancamento')


def pesquisar_lancamento(request):
    reg_per_page = 10
    total_lancamentos_list = Lancamento.objects.order_by('id')
    lancamentos = paginattion_create(total_lancamentos_list, reg_per_page, request)

    query_lancamentos = request.GET.get('descricao')

    if query_lancamentos:
        total_lancamentos_list = total_lancamentos_list.filter(descricao__icontains=query_lancamentos)
        lancamentos = paginattion_create(total_lancamentos_list, reg_per_page, request)
        return render(request, 'lacamento/pesquisar_lancamento.html', {'lancamentos': lancamentos})

    return render(request, 'lacamento/pesquisar_lancamento.html', {'lancamentos': lancamentos})


def listar_lancamentos(request):
    reg_per_page = 10
    total_lancamentos_list = Lancamento.objects.filter(status_lancamento=1).order_by('id')
    lancamentos = paginattion_create(total_lancamentos_list, reg_per_page, request)

    query_data_inicial = request.GET.get('data_inicial')
    query_data_final = request.GET.get('data_final')

    if query_data_inicial or query_data_final:
        total_lancamentos_list = total_lancamentos_list.filter(data_vencimento__range=(query_data_inicial, query_data_final))
        lancamentos = paginattion_create(total_lancamentos_list, reg_per_page, request)
        return render(request, 'lacamento/listar_faturar_lancamento.html', {'lancamentos': lancamentos})

    return render(request, 'lacamento/listar_faturar_lancamento.html', {'lancamentos': lancamentos})


def faturar_lancamento(request, pk):
    lancamento = get_object_or_404(Lancamento, pk=pk)
    query_data_pagamento = request.GET.get('data_vencimento')
    # data_pagamento = datetime.strptime(query_data_pagamento, "%d/%m/%y")

    if request.method == 'POST':
        Lancamento.objects.filter(pk=pk).update(data_pagamento=query_data_pagamento)
        Lancamento.objects.filter(pk=pk).update(status_lancamento_id=3)
        return redirect('controle_fin:listar_lancamento')

    else:
        return render(request, 'lacamento/faturar_lancamento.html', {'lancamento': lancamento})