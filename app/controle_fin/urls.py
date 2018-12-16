from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path
from SGFIN.settings import base
from app.controle_fin.views import agencia_views, cliente_views, \
    tipo_lancamento_views, lancamento_views
from .views import banco_views

app_name = 'controle_fin'

urlpatterns = [
    #Banco
    url(r'^cadastro-banco/$', banco_views.cadastrar_banco, name='cadastrar_banco'),
    url(r'^pesquisa-banco/$', banco_views.pesquisar_banco, name='pesquisar_banco'),
    url(r'^cadastro-banco/(?P<pk>[0-9]+)/editar/$', banco_views.editar_banco, name='editar_banco'),
    url(r'^cadastro-banco/(?P<pk>[0-9]+)/delete/$', banco_views.excluir_banco, name='deletar_banco'),
    # Agencia
    url(r'^cadastro-agencia/$', agencia_views.cadastrar_agencia, name='cadastrar_agencia'),
    url(r'^pesquisa-agencia/$', agencia_views.pesquisar_agencia, name='pesquisar_agencia'),
    url(r'^cadastro-agencia/(?P<pk>[0-9]+)/editar/$', agencia_views.editar_agencia, name='editar_agencia'),
    url(r'^cadastro-agencia/(?P<pk>[0-9]+)/delete/$', agencia_views.excluir_agencia, name='deletar_agencia'),
    # Cliente
    url(r'^cadastro-cliente/$', cliente_views.cadastrar_cliente, name='cadastrar_cliente'),
    url(r'^pesquisa-cliente/$', cliente_views.pesquisar_cliente, name='pesquisar_cliente'),
    url(r'^cadastro-cliente/(?P<pk>[0-9]+)/editar/$', cliente_views.editar_cliente, name='editar_cliente'),
    url(r'^cadastro-cliente/(?P<pk>[0-9]+)/delete/$', cliente_views.excluir_cliente, name='deletar_cliente'),
    # Tipo de Lancamento
    url(r'^cadastro-tipo_lancamento/$', tipo_lancamento_views.cadastrar_tipo_lancamento, name='cadastrar_tipo_lancamento'),
    url(r'^pesquisa-tipo_lancamento/$', tipo_lancamento_views.pesquisar_tipo_lancamento, name='pesquisar_tipo_lancamento'),
    url(r'^cadastro-tipo_lancamento/(?P<pk>[0-9]+)/editar/$', tipo_lancamento_views.editar_tipo_lancamento, name='editar_tipo_lancamento'),
    url(r'^cadastro-tipo_lancamento/(?P<pk>[0-9]+)/delete/$', tipo_lancamento_views.excluir_tipo_lancamento, name='deletar_tipo_lancamento'),
    # Lancamentos
    url(r'^cadastro-lancamento/$', lancamento_views.cadastrar_lancamento, name='cadastrar_lancamento'),
    url(r'^pesquisa-lancamento/$', lancamento_views.pesquisar_lancamento, name='pesquisar_lancamento'),
    url(r'^cadastro-lancamento/(?P<pk>[0-9]+)/editar/$', lancamento_views.editar_lancamento, name='editar_lancamento'),
    url(r'^cadastro-lancamento/(?P<pk>[0-9]+)/delete/$', lancamento_views.excluir_lancamento, name='deletar_lancamento'),
]