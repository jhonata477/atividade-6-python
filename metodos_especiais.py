
from abc import ABC, abstractmethod


class Conta(ABC):

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    @abstractmethod
    def calcular_rendimento(self):
        pass

    # Representação amigável
    def __str__(self):
        return f"Titular: {self.titular} | Saldo: R$ {self.saldo:.2f}"

    # Representação técnica
    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"(titular={self.titular!r}, saldo={self.saldo!r})"
        )

    # Compara duas contas pelo saldo
    def __eq__(self, outra):
        if not isinstance(outra, Conta):
            return NotImplemented
        return self.saldo == outra.saldo

    # Compara contas pelo saldo
    def __lt__(self, outra):
        if not isinstance(outra, Conta):
            return NotImplemented
        return self.saldo < outra.saldo


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
