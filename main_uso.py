#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------
import copy
from itertools import product
from classes.PessoaFisica import PessoaFisica
from classes.Endereco import Endereco
from classes.Produto import Produto
from classes.Carrinho import Carrinho
from classes.Pedido import Pedido
from classes.Pagamentos import Pagamento

pessoa1 = PessoaFisica('524.222.452-6', 'tiago@email.com', 'Carlos')
end1 = Endereco('08320330', 430)
end2 = Endereco('04546042', 300)
pessoa1.adicionar_endereco('casa', end1)
pessoa1.adicionar_endereco('trabalho', end2)
sabonete = Produto("0010342967", "Sabonete")

pessoas = PessoaFisica.busca_nome('Carlos')
if len(pessoas) > 0:
    pessoa = pessoas[0]  #Pega a primeira pessoa

produtos = Produto.busca_nome("sabon")
if len(produtos) > 0: 
    produto = produtos[0]

ends = pessoa.listar_enderecos()
if len(ends) > 0:
    endereco = ends['casa']

carrinho = Carrinho()
carrinho.adicionar_item(sabonete, 2)

pedido = Pedido()
pedido.endereco_entrega = copy.deepcopy(endereco) 
pedido.endereco_faturamento = copy.deepcopy(endereco)
pedido.compras = carrinho.itens 
pedido.pessoa = pessoa1

pag = Pagamento(pedido)
pag.processa_pagamento()
if pag.pagamento_aprovado:
    pedido.status = Pedido.PAGO 

print("Pedido aguardando coleta")

## Pedido deve imprir todos os detalhes da compra - pessoa, endereço e produtos
print(pedido)