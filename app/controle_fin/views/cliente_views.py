from django.shortcuts import render, redirect, get_object_or_404
from app.controle_fin.forms.cliente_forms import ClienteForm
from app.controle_fin.models.cliente_models import Cliente
from app.controle_fin.utils.utils import paginattion_create


def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('controle_fin:cadastrar_cliente')
    else:
        form = ClienteForm()
        return render(request, 'cliente/cadastrar_cliente.html', {'form': form})


def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('controle_fin:pesquisar_cliente')
    else:
        form = ClienteForm(instance=cliente)
        return render(request, 'cliente/editar_cliente.html', {'form': form})


def excluir_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    return redirect('controle_fin:pesquisar_cliente')


def pesquisar_cliente(request):
    reg_per_page = 10
    total_clientes_list = Cliente.objects.order_by('id')
    clientes = paginattion_create(total_clientes_list, reg_per_page, request)

    query_email = request.GET.get('email')
    query_nome = request.GET.get('nome')

    if query_email and query_nome:
        total_clientes_list = total_clientes_list.filter(email__icontains=query_email) | total_clientes_list.filter(nome__icontains=query_nome)
        clientes = paginattion_create(total_clientes_list, reg_per_page, request)
        return render(request, 'cliente/pesquisar_cliente.html', {'clientes': clientes})

    if query_email or query_nome:
        if query_email:
            total_clientes_list = total_clientes_list.filter(email__icontains=query_email)
            clientes = paginattion_create(total_clientes_list, reg_per_page, request)
            return render(request, 'cliente/pesquisar_cliente.html', {'clientes': clientes})
        else:
            total_clientes_list = total_clientes_list.filter(nome__icontains=query_nome)
            clientes = paginattion_create(total_clientes_list, reg_per_page, request)
            return render(request, 'cliente/pesquisar_cliente.html', {'clientes': clientes})

    return render(request, 'cliente/pesquisar_cliente.html', {'clientes': clientes})
