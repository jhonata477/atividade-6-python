
from abc import ABC, abstractmethod


# 1. Classe abstrata
class RegistroBase(ABC):

    def __init__(self, email):
        self.email = email

    @abstractmethod
    def validar(self):
        pass


# 2. Classe que herda da classe abstrata
class RegistroPessoa(RegistroBase):

    def __init__(self, email, cpf, telefone, data):
        super().__init__(email)
        self.cpf = cpf
        self.telefone = telefone
        self.data = data

    def validar(self):
        return (
            "@" in self.email
            and len(self.cpf) == 14
            and len(self.telefone) >= 13
            and len(self.data) == 10
        )


# 3. Classe para registros válidos
class RegistroValido(RegistroPessoa):

    def exibir(self):
        print(f"Registro válido: {self.email}")


# 4. Classe para registros inválidos
class RegistroInvalido(RegistroPessoa):

    def exibir(self):
        print(f"Registro inválido: {self.email}")
