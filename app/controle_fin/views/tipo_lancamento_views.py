from django.shortcuts import render, redirect, get_object_or_404
from SGFIN.settings.base import n_page
from app.controle_fin.forms.tipo_lancamento_forms import TipoLancamentoForm
from app.controle_fin.models.tipo_lancamento_models import TipoLancamento
from app.controle_fin.utils.utils import paginattion_create


def cadastrar_tipo_lancamento(request):
    if request.method == 'POST':
        form = TipoLancamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('controle_fin:cadastrar_tipo_lancamento')
    else:
        form = TipoLancamentoForm()
        return render(request, 'tipo_lancamento/cadastrar_tipo_lancamento.html', {'form': form})


def editar_tipo_lancamento(request, pk):
    tipo_despesa = get_object_or_404(TipoLancamento, pk=pk)
    if request.method == 'POST':
        form = TipoLancamentoForm(request.POST, instance=tipo_despesa)
        if form.is_valid():
            form.save()
            return redirect('controle_fin:pesquisar_tipo_lancamento')
    else:
        form = TipoLancamentoForm(instance=tipo_despesa)
        return render(request, 'tipo_lancamento/editar_tipo_lancamento.html', {'form': form})


def excluir_tipo_lancamento(request, pk):
    tipo_despesa = get_object_or_404(TipoLancamento, pk=pk)
    tipo_despesa.delete()
    return redirect('controle_fin:pesquisar_tipo_lancamento')


def pesquisar_tipo_lancamento(request):
    reg_per_page = n_page
    total_tp_despesa_list = TipoLancamento.objects.order_by('id')
    tp_despesas = paginattion_create(total_tp_despesa_list, reg_per_page, request)

    query_tp_despesa = request.GET.get('tipo_lancamento')

    if query_tp_despesa:
        total_tp_despesa_list = total_tp_despesa_list.filter(tipo_lancamento__icontains=query_tp_despesa)
        tp_despesas = paginattion_create(total_tp_despesa_list, reg_per_page, request)
        return render(request, 'tipo_lancamento/pesquisar_tipo_lancamento.html', {'tp_lancamentos': tp_despesas})

    return render(request, 'tipo_lancamento/pesquisar_tipo_lancamento.html', {'tp_lancamentos': tp_despesas})