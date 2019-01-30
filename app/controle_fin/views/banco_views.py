from django.shortcuts import render, redirect, get_object_or_404
from app.controle_fin.forms.banco_form import CadastroBancoForm
from app.controle_fin.models.banco_models import Banco
from app.controle_fin.utils.utils import paginattion_create


def cadastrar_banco(request):
    if request.method == 'POST':
        form = CadastroBancoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('controle_fin:cadastrar_banco')
    else:
        cadastro_banco_list = Banco.objects.all()
        bancos = paginattion_create(cadastro_banco_list, 10, request)
        form = CadastroBancoForm()
        return render(request, 'banco/cadastro_banco.html', {
            'form': form,
            'bancos': bancos
        })


def pesquisar_banco(request):
    reg_per_page = 5
    all_bancos_list = Banco.objects.order_by('id')
    all_bancos = paginattion_create(all_bancos_list, reg_per_page, request)

    query_codigo = request.GET.get('codigo')
    query_nome = request.GET.get('nome_banco')

    if query_codigo is None:
        query_codigo = ''

    if query_nome is None:
        query_nome = ''

    if query_codigo and query_nome:
        all_bancos_list = all_bancos_list.filter(codigo__icontains=query_codigo)|all_bancos_list.filter(nome_banco__icontains=query_nome)
        all_bancos = paginattion_create(all_bancos_list, reg_per_page, request)
        return render(request, 'banco/pesquisar_banco.html', {
            'bancos': all_bancos,
            'query_codigo': query_codigo,
            'query_nome': query_nome
        })

    if query_nome or query_codigo:
        if query_codigo:
            all_bancos_list = all_bancos_list.filter(codigo__icontains=query_codigo)
            all_bancos = paginattion_create(all_bancos_list, reg_per_page, request)
            return render(request, 'banco/pesquisar_banco.html', {
                'bancos': all_bancos,
                'query_codigo': query_codigo,
                'query_nome': query_nome
            })

        else:
            all_bancos_list = all_bancos_list.filter(nome_banco__icontains=query_nome)
            all_bancos = paginattion_create(all_bancos_list, reg_per_page, request)
            return render(request, 'banco/pesquisar_banco.html', {
                'bancos': all_bancos,
                'query_codigo': query_codigo,
                'query_nome': query_nome
            })

    return render(request, 'banco/pesquisar_banco.html', {
        'bancos': all_bancos,
        'query_codigo': query_codigo,
        'query_nome': query_nome
    })


def editar_banco(request, pk):
    banco = get_object_or_404(Banco, pk=pk)
    if request.method == 'POST':
        form = CadastroBancoForm(request.POST, instance=banco)
        if form.is_valid():
            form.save()
            return redirect('controle_fin:pesquisar_banco')
    else:
        form = CadastroBancoForm(instance=banco)
        return render(request, 'banco/editar_banco.html', {'form': form})


def excluir_banco(request, pk):
    banco = get_object_or_404(Banco, pk=pk)
    banco.delete()
    return redirect('controle_fin:pesquisar_banco')