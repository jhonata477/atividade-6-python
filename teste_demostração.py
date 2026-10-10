
from modelos import ContaCorrente, ContaPoupanca


# Criando 10 objetos (instâncias)
contas = [
    ContaCorrente("João", 1000, 500),
    ContaPoupanca("Maria", 2000, 0.5),
    ContaCorrente("Pedro", 1500, 300),
    ContaPoupanca("Ana", 3000, 0.6),
    ContaCorrente("Lucas", 800, 200),
    ContaPoupanca("Julia", 2500, 0.4),
    ContaCorrente("Carlos", 1200, 400),
    ContaPoupanca("Beatriz", 4000, 0.7),
    ContaCorrente("Rafael", 900, 250),
    ContaPoupanca("Larissa", 3500, 0.5)
]


# Demonstração de polimorfismo
print("===== DEMONSTRAÇÃO DE POLIMORFISMO =====")

for conta in contas:
    print(conta)
    print(f"Rendimento: R$ {conta.calcular_rendimento():.2f}")
    print("-" * 40)


# Testando entradas inválidas
print("\n===== TESTE DE EXCEÇÕES =====")

try:
    conta_teste = ContaCorrente("Marcos", -500, 200)
except ValueError as erro:
    print(f"Erro ao criar conta: {erro}")

try:
    conta_teste = ContaPoupanca("Paula", 1000, 150)
except ValueError as erro:
    print(f"Erro ao criar poupança: {erro}")


# Testando comparação e ordenação
print("\n===== CONTAS ORDENADAS POR SALDO =====")

contas.sort()

for conta in contas:
    print(conta)


# Estatísticas
print("\n===== ESTATÍSTICAS =====")

total = len(contas)
saldo_total = sum(conta.saldo for conta in contas)
media = saldo_total / total

print(f"Total de contas: {total}")
print(f"Soma dos saldos: R$ {saldo_total:.2f}")
print(f"Média dos saldos: R$ {media:.2f}")
