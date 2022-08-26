
class Pagamento:

    def __init__(self, pedido):
        self.pedido = pedido 
        self.pago = False

    def processa_pagamento(self):
        pass 

    # Função dummy que sempre dá o pagamento como aprovado
    def pagamento_aprovado():
        return True

    