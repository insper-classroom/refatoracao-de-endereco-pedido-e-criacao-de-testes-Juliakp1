#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------



class Produto:

    todosProdutos = []

    def __init__(self, id, nome=''):
        self.id = id
        self.nome = nome
        Produto.todosProdutos += [self]

    def set_id(self, novoId):
        self.id = novoId

    def get_id(self):
        return self.id
    
    def __str__(self):
        return self.nome

    def busca_nome(busca):

        finalList = []
        for product in Produto.todosProdutos:
            if busca in product.nome:
                finalList += [product]

        return finalList
