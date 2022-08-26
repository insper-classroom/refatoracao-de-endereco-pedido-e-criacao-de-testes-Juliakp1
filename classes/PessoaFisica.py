#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
import re



class PessoaFisica:
    '''Esta classe implementa uma pessoa no contexto de uma compra em e-commerce.
    
    As propriedades email e cpf estão privadas para previnir o usuário da classe de 
    acessar e alterar diretamente a propriedade sem uma verificação.
    '''

    todasPessoas = []

    def __init__(self, cpf, email, nome='Visitante'):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.__enderecos = {}
        PessoaFisica.todasPessoas += [self]

    # escolher o estilo de retorno

    def adicionar_endereco(self, apelido_endereco, end:Endereco):
        numb = str(end.cep)
        self.__enderecos[apelido_endereco] = numb

    def remover_endereco(self, apelido_endereco):
        pass

    def get_endereco(self, apelido_endereco):
        pass

    def listar_enderecos(self):
        dictio = self.__enderecos
        return dictio

    def __str__(self):
        return self.nome + ' - ' + str(self.__enderecos)

    def busca_nome(busca):

        finalList = []
        for person in PessoaFisica.todasPessoas:
            print(busca, person.nome)
            if busca in person.nome:
                finalList += [person]

        return finalList
