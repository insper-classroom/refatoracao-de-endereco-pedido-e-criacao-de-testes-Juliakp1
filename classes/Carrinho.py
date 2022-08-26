#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  :
# Created Date:
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
from classes.Produto import Produto
from classes.PessoaFisica import PessoaFisica

# Esta classe deverá permitir a inserção de items, bem como a atualização da quantidade de
# produtos em um item

class Carrinho:

    def __init__(self):
        # Chave é o id do Produto e o Valor é a quantidade desse item no carrinho
        self.itens = {}

    def adicionar_item(self, item:Produto, qtd):

        if item in self.itens:
            self.itens[item] += qtd
        else:
            self.itens[item] = qtd

    def remover_item(self, item:Produto):

        id = item.get_id()
        del self.itens[id]

    def lista_itens(compras):

        newList = []
        for item in compras.keys():
            newList.append(str(item) + str(compras[item]))

        return newList
