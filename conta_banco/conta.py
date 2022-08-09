
from wsgiref.validate import validator


class Conta:

    def __init__(self, numero, nome, saldo, limite):
        self.__numero = numero
        self.__nome = nome
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(self.__saldo)

    def depositar(self, valor):
        self.__saldo += valor

    def valida_saque(self, valor_sacar):
        return valor_sacar <= (self.__saldo + self.__limite)

    def sacar(self, valor):
        if(self.valida_saque):
            self.__saldo -= valor
        else:
            print("limite insuficiente")
        
    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def nome(self):
        return self.__nome

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def cod_banco():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}
