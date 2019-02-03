from django.shortcuts import render, redirect, get_object_or_404
from SGFIN.settings.base import n_page
from app.controle_fin.forms.agencia_forms import AgenciaForm
from app.controle_fin.models.agencia_models import Agencia
from app.controle_fin.models.banco_models import Banco
from app.controle_fin.utils.utils import paginattion_create


def cadastrar_agencia(request):
    if request.method == 'POST':
        form = AgenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('controle_fin:cadastrar_agencia')
    else:
        form = AgenciaForm()
        form.fields['banco'].queryset = Banco.objects.filter(status_id=1)
        return render(request, 'agencia/cadastrar_agencia.html', {'form': form})


def editar_agencia(request, pk):
    agencia = get_object_or_404(Agencia, pk=pk)
    if request.method == 'POST':
        form = AgenciaForm(request.POST, instance=agencia)
        if form.is_valid():
            form.save()
            return redirect('controle_fin:pesquisar_agencia')
    else:
        form = AgenciaForm(instance=agencia)
        form.fields['banco'].queryset = Banco.objects.filter(status_id=1)
        return render(request, 'agencia/editar_agencia.html', {'form': form})


def excluir_agencia(request, pk):
    agencia = get_object_or_404(Agencia, pk=pk)
    agencia.delete()
    return redirect('controle_fin:pesquisar_agencia')


def pesquisar_agencia(request):
    reg_per_page = n_page
    all_agencia_list = Agencia.objects.order_by('id')
    all_agencia = paginattion_create(all_agencia_list, reg_per_page, request)

    query_codigo = request.GET.get('codigo_agencia')
    query_nome_banco = request.GET.get('nome_banco')
    query_nome_agencia = request.GET.get('nome_agencia')

    if query_codigo and query_nome_banco and query_nome_agencia:
        all_agencia_list = all_agencia_list.filter(codigo_agencia__icontains=query_codigo)|all_agencia_list.filter(banco__icontains=query_nome_banco)|all_agencia_list.filter(nome_agencia__icontains=query_nome_agencia)
        all_agencia = paginattion_create(all_agencia_list, reg_per_page, request)
        return render(request, 'agencia/pesquisar_agencia.html', {'agencias': all_agencia})
    if query_nome_banco or query_codigo or query_nome_agencia:
        if query_codigo:
            all_agencia_list = all_agencia_list.filter(codigo_agencia__icontains=query_codigo)
            all_agencia = paginattion_create(all_agencia_list, reg_per_page, request)
            return render(request, 'agencia/pesquisar_agencia.html', {'agencias': all_agencia})
        elif query_nome_banco:
            all_agencia_list = all_agencia_list.filter(banco__icontains=query_nome_banco)
            all_agencia = paginattion_create(all_agencia_list, reg_per_page, request)
            return render(request, 'agencia/pesquisar_agencia.html', {'agencias': all_agencia})
        else:
            all_agencia_list = all_agencia_list.filter(nome_agencia__icontains=query_nome_agencia)
            all_agencia = paginattion_create(all_agencia_list, reg_per_page, request)
            return render(request, 'agencia/pesquisar_agencia.html', {'agencias': all_agencia})

    return render(request, 'agencia/pesquisar_agencia.html', {'agencias': all_agencia})