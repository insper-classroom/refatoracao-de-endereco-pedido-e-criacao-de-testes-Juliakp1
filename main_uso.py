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
print(pessoa1.listar_enderecos())

sabonete = Produto("0010342967", "Sabonete")
chocolate = Produto("703288402", "Chocolate")
print(sabonete)

carrinho = Carrinho()
carrinho.adicionar_item(sabonete, 2)

pedido = Pedido()
# Lembre-se de adicionar estes atributos ao endereço
pedido.endereco_entrega = copy.deepcopy(end1) 
pedido.endereco_faturamento = copy.deepcopy(end2)

pag = Pagamento(pedido)
print('here! |/_')
print(pedido)