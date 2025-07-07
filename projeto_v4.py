
from datetime import date
from abc import ABC, abstractmethod

usuarios = []
contas_correntes = []

class Historico():
    def __init__(self):
        self._transacoes = []

    def adicionar_transacao(self, transacao:"Transacao"):
        self._transacoes.append(transacao)

class Conta():
    def __init__(self, numero:int, agencia:str, cliente:"Cliente"):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = Historico()

    def saldo(self)->float:
        return self._saldo
    
    @staticmethod
    def nova_conta(cliente:"Cliente", numero:int)->"Conta":
        return Conta (numero=numero, agencia="0001", cliente=cliente)
    
    def sacar(self, valor:float)->bool:
        if valor <= self._saldo:
            self._saldo -= valor
            return True
        return False
    
    def depositar(self, valor:float):
         if valor > 0:
             self._saldo += valor
             return True
         return False

class ContaCorrente(Conta):
    def __init__(self, numero:int, agencia:str, cliente:"Cliente", limite:float, limite_saques:int):
        super().__init__(numero, agencia, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

class Cliente():
    def __init__(self, endereco:str):
        self._endereco = endereco
        self._contas = []
    
    def realizar_transacao(self, conta:Conta, transacao:"Transacao"):
        if transacao.registrar(conta):
            conta._historico.adicionar_transacao(transacao)
    
    def adicionar_conta(self, conta:Conta):
        self._contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf:str, nome:str, data_nascimento:date):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta:Conta)->bool:
        pass
    
class Deposito(Transacao):
    def __init__(self, valor:float):
        super().__init__()
        self._valor = valor
    
    def registrar(self, conta):
        return conta.depositar(self._valor)

class Saque(Transacao):
    def __init__(self, valor:float):
        super().__init__()
        self._valor = valor

    def registrar(self, conta):
        return conta.sacar(self._valor)
def encontrar_usuario_por_cpf(cpf, usuarios):
    cpf = formatar_cpf(cpf)
    for cliente in usuarios:
        if cliente._cpf == cpf:
            return cliente
    return None

def selecionar_conta(cliente):
    if not cliente._contas:
        print("Cliente não possui contas.")
        return None
    return cliente._contas[0]

def exibir_extrato(conta):
    print("\n### EXTRATO ###")
    transacoes = conta._historico._transacoes
    if not transacoes:
        print("Nenhuma movimentação registrada.")
    else:
        for transacao in transacoes:
            tipo = transacao.__class__.__name__
            valor = transacao._valor
            print(f"{tipo}: R$ {valor:.2f}")
    print(f"Saldo atual: R$ {conta.saldo():.2f}")

def formatar_cpf(cpf):
    return cpf.replace(".", "").replace("-", "").strip()


while True:
    print("\nBem-Vindo ao Banco SantANDRÉ.")
    print(">> O SEU banco <<")
    print("""
            [1] -> Depósito
            [2] -> Saque
            [3] -> Extrato
            [4] -> Criar Usuário
            [5] -> Criar Conta Corrente
            [6] -> Listar Contas
            [0] -> Sair
        """)
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cpf = input("CPF do titular: ")
        cliente = encontrar_usuario_por_cpf(cpf, usuarios)

        if not cliente:
            print("Cliente não encontrado")
            continue

        conta = selecionar_conta(cliente)
        if not conta:
            continue

        valor = float(input("Informe o valor do depósito: "))
        transacao = Deposito(valor)
        cliente.realizar_transacao(conta, transacao)

    elif opcao == "2":
        cpf = input("CPF do titular: ")
        cliente = encontrar_usuario_por_cpf(cpf, usuarios)

        if not cliente:
            print("Cliente não encontrado")
            continue

        conta = selecionar_conta(cliente)
        if not conta:
            continue

        valor = float(input("Informe o valor do saque: "))
        transacao = Saque(valor)
        cliente.realizar_transacao(conta, transacao)

    elif opcao == "3":
        cpf = input("CPF do titular: ")
        cliente = encontrar_usuario_por_cpf(cpf, usuarios)

        if not cliente:
            print("Cliente não encontrado")
            continue

        conta = selecionar_conta(cliente)
        if not conta:
            continue

        exibir_extrato(conta)

    elif opcao == "4":
        nome = input("Nome completo: ")
        data_nascimento = input("Data de nascimento:(AAAA-MM-DD) ")
        cpf = formatar_cpf(input("CPF (Apenas números): "))
        endereco = input("Endereço (logradouro, número - bairro - cidade/UF): ")

        if cpf in [u._cpf for u in usuarios]:
            print("CPF já cadastrado")
            continue

        novo_user = PessoaFisica(endereco, cpf, nome, date.fromisoformat(data_nascimento))
        usuarios.append(novo_user)
        print("Usuário cadastrado com sucesso!")

    elif opcao == "5":
        cpf = input("Informe o CPF do usuário: ")
        cliente = encontrar_usuario_por_cpf(cpf, usuarios)

        if not cliente:
            print("Cliente não encontrado.")
            continue

        numero_conta = len(contas_correntes) + 1
        nova_conta = ContaCorrente(numero_conta, "0001", cliente, limite=500.0, limite_saques=3)
        cliente.adicionar_conta(nova_conta)
        contas_correntes.append(nova_conta)
        print(f"Conta criada com sucesso! Agência: 0001 | Conta: {numero_conta}")

    elif opcao == "6":
        for conta in contas_correntes:
            titular = conta._cliente._nome
            print(f"Agência: {conta._agencia} | Conta: {conta._numero} | Titular: {titular}")

    elif opcao == "0":
        print("Obrigado por usar o Banco SantANDRÉ. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")



