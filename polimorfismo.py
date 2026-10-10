
from abc import ABC, abstractmethod


class Conta(ABC):

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    @abstractmethod
    def calcular_rendimento(self):
        pass


class ContaCorrente(Conta):

    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self.limite = limite

    def calcular_rendimento(self):
        # Conta corrente não gera rendimento neste exemplo
        return 0


class ContaPoupanca(Conta):

    def __init__(self, titular, saldo, taxa):
        super().__init__(titular, saldo)
        self.taxa = taxa

    def calcular_rendimento(self):
        # Calcula o rendimento da poupança
        return self.saldo * self.taxa / 100
