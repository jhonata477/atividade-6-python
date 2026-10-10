
from abc import ABC, abstractmethod


# 1. Classe abstrata
class Conta(ABC):

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, nome):
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("O nome do titular não pode ficar vazio.")
        self._titular = nome.strip()

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)) or isinstance(valor, bool):
            raise ValueError("O saldo deve ser um número.")
        if valor < 0:
            raise ValueError("O saldo não pode ser negativo.")
        self._saldo = valor

    @abstractmethod
    def calcular_rendimento(self):
        pass

    def __str__(self):
        return f"Titular: {self.titular} | Saldo: R$ {self.saldo:.2f}"


# 2. Conta corrente
class ContaCorrente(Conta):

    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self.limite = limite

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, valor):
        if not isinstance(valor, (int, float)) or isinstance(valor, bool):
            raise ValueError("O limite deve ser um número.")
        if valor < 0:
            raise ValueError("O limite não pode ser negativo.")
        self._limite = valor

    def calcular_rendimento(self):
        return 0

    def __str__(self):
        return (
            f"Conta Corrente | Titular: {self.titular} | "
            f"Saldo: R$ {self.saldo:.2f} | "
            f"Limite: R$ {self.limite:.2f}"
        )


# 3. Conta poupança
class ContaPoupanca(Conta):

    def __init__(self, titular, saldo, taxa_rendimento):
        super().__init__(titular, saldo)
        self.taxa_rendimento = taxa_rendimento

    @property
    def taxa_rendimento(self):
        return self._taxa_rendimento

    @taxa_rendimento.setter
    def taxa_rendimento(self, valor):
        if not isinstance(valor, (int, float)) or isinstance(valor, bool):
            raise ValueError("A taxa deve ser um número.")
        if not 0 <= valor <= 100:
            raise ValueError("A taxa deve estar entre 0 e 100.")
        self._taxa_rendimento = valor

    def calcular_rendimento(self):
        return self.saldo * self.taxa_rendimento / 100

    def __str__(self):
        return (
            f"Conta Poupança | Titular: {self.titular} | "
            f"Saldo: R$ {self.saldo:.2f} | "
            f"Rendimento: R$ {self.calcular_rendimento():.2f}"
        )


# 4. Cliente
class Cliente:

    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O nome não pode ficar vazio.")
        self._nome = valor.strip()

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, valor):
        if not isinstance(valor, str) or len(valor) != 14:
            raise ValueError("O CPF deve estar no formato 000.000.000-00.")
        self._cpf = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if not isinstance(valor, str) or "@" not in valor or "." not in valor.split("@")[-1]:
            raise ValueError("E-mail inválido.")
        self._email = valor

    def __str__(self):
        return f"Cliente: {self.nome} | CPF: {self.cpf} | E-mail: {self.email}"
