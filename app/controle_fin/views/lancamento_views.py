from datetime import date, datetime
from django.shortcuts import render, redirect, get_object_or_404
from app.controle_fin.forms.lancamento_forms import LancamentoForm
from app.controle_fin.models.lancamento_models import Lancamento, \
    StatusLancamento
from app.controle_fin.utils.utils import paginattion_create



def cadastrar_lancamento(request):
    if request.method == 'POST':
        form = LancamentoForm(request.POST)
        print(form)
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