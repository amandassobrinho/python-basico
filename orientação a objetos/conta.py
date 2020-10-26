class Conta:
    def __init__(self,clientes,numero_conta,saldo_inicial):
        self.__clientes = clientes
        self.__numero_conta = numero_conta
        self.__saldo = saldo_inicial
        self.__operacoes = []
        self.__operacoes.append(("saldo_inicial",self.__saldo))
    def sacar (self,valor):
        if valor > self.__saldo :
            raise ValueError()
        self.__saldo = self.__saldo - valor
        self.__operacoes.append(("saque",valor))
    def depositar (self,valor):
        self.__saldo = self.__saldo + valor
        self.__operacoes.append(("deposito",valor))
    def tirar_extrato(self):
        return self.__operacoes
    @property
    def clientes(self):
        return self.__clientes  
    @property
    def numero(self):
        return self.__numero_conta
    @property
    def saldo(self):
        return self.__saldo
 
    
