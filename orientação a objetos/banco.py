from conta import Conta
from cliente import Cliente
class Banco:
    def __init__(self,nome):
        self.__nome = nome
        self.__contas = []
        self.__ultimaconta = 0 
    def abre_conta(self,lista_clientes,saldo_inicial):
        if saldo_inicial < 0:
            raise ValueError()
        else:
            self.__contas.append(Conta(lista_clientes, self.__ultimaconta + 1, saldo_inicial))
            self.__ultimaconta = self.__ultimaconta + 1 
    @property
    def nome(self):
        return self.__nome
    @property
    def contas (self):
        return self.__contas
