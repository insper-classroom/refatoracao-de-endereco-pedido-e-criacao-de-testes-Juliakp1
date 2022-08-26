#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  :
# Created Date:
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica
from classes.Carrinho import Carrinho
import re




class Pedido:
    EM_ABERTO = 1
    PAGO = 2

    def __init__(self):
        self.compras = []
        self.pessoa = []
        self.endereco_entrega = ''
        self.endereco_faturamento = ''
    
    def __str__(self):

        listy = str(self.compras)
        nome = str(self.pessoa)
        return nome + ' comprou: ' + listy
        
    