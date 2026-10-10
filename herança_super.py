
from abc import ABC, abstractmethod


# Classe mãe
class Conta(ABC):

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    @abstractmethod
    def calcular_rendimento(self):
        pass

    def __str__(self):
        return f"Titular: {self.titular} | Saldo: R$ {self.saldo:.2f}"


# Classe filha: ContaCorrente é uma Conta
class ContaCorrente(Conta):

    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self.limite = limite

    def calcular_rendimento(self):
        return 0

    def __str__(self):
        return (
            f"Conta Corrente | {super().__str__()} | "
            f"Limite: R$ {self.limite:.2f}"
        )


# Classe filha: ContaPoupanca é uma Conta
class ContaPoupanca(Conta):

    def __init__(self, titular, saldo, taxa):
        super().__init__(titular, saldo)
        self.taxa = taxa

    def calcular_rendimento(self):
        return self.saldo * self.taxa / 100

    def __str__(self):
        return (
            f"Conta Poupança | {super().__str__()} | "
            f"Rendimento: R$ {self.calcular_rendimento():.2f}"
        )
