import pytest
from classes.Endereco import Endereco

def test_limpa_input():
    cep1 = '08320-330'
    cep2 = 8320330
    numero = 423
    end1 = Endereco(cep1, numero)
    end2 = Endereco(cep2, numero)
    assert end1.consultar_cep(cep1) == end2.consultar_cep(cep2)

def test_cep_invalido():
    cep = '12345678'
    assert False == Endereco.consultar_cep(cep, cep)

def test_cep_muito_pequeno():
    cep = '000'
    assert False == Endereco.consultar_cep(cep, cep)