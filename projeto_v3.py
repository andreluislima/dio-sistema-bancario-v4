# SISTEMA BANCÁRIO - V3

from datetime import date
from abc import ABC, abstractmethod


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


# saldo = 0
# extrato = []
# real = "R$ "
# numero_saques = 0

# contas_correntes = []
# usuarios = []
# cpf_cadastrados = set()


# def menu():
#     print("\nBem-Vindo ao Banco SantANDRÉ.")
#     print(">> O SEU banco <<")
#     print("""
#         [1] -> Depósito
#         [2] -> Saque
#         [3] -> Extrato
#         [4] -> Criar Usuário
#         [5] -> Criar Conta Corrente
#         [6] -> Listar Contas
#         [0] -> Sair
#     """)


# def deposito(saldo, valor, extrato, /):
#     if valor > 0:
#         saldo += valor
#         extrato.append(f"Depósito: {real}{valor:.2f}")
#         print("Depósito realizado com sucesso!")
#     else:
#         print("Valor inválido para depósito.")
#     return saldo, extrato


# def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
#     if numero_saques >= limite_saques:
#         print("Limite de saques diário excedido.")
#     elif valor > limite:
#         print("Valor excede o limite por saque.")
#     elif valor > saldo:
#         print("Saldo insuficiente.")
#     elif valor > 0:
#         saldo -= valor
#         extrato.append(f"Saque: {real}{valor:.2f}")
#         numero_saques += 1
#         print("Saque realizado com sucesso!")
#     else:
#         print("Valor inválido para saque.")
#     return saldo, extrato, numero_saques


# def op_extrato(saldo, *, extrato):
#     print("\n### EXTRATO ###")
#     if extrato:
#         for item in extrato:
#             print(item)
#     else:
#         print("Nenhuma movimentação registrada.")
#     print(f"Saldo atual: {real}{saldo:.2f}")


# def formatar_cpf(cpf):
#     cpf = cpf.replace(".", "").replace("-", "").strip()
#     return cpf if len(cpf) == 11 else None


# def formatar_data(data):
#     partes = data.strip().split("/")
#     return f"{partes[0]}/{partes[1]}/{partes[2]}" if len(partes) == 3 else None


# def novo_usuario(nome, data_nascimento, cpf, endereco):
#     cpf = formatar_cpf(cpf)
#     data_nascimento = formatar_data(data_nascimento)
#     if not cpf or not data_nascimento:
#         print("Dados inválidos. Usuário não cadastrado.")
#         return
#     if cpf in cpf_cadastrados:
#         print("CPF já cadastrado.")
#         return
#     usuario = {
#         "nome": nome.strip().title(),
#         "data_nascimento": data_nascimento,
#         "cpf": cpf,
#         "endereco": endereco.strip()
#     }
#     usuarios.append(usuario)
#     cpf_cadastrados.add(cpf)
#     print("Usuário cadastrado com sucesso!")


# def encontrar_usuario(cpf):
#     for usuario in usuarios:
#         if usuario["cpf"] == cpf:
#             return usuario
#     return None


# def nova_conta_corrente(usuario):
#     agencia = "0001"
#     numero_conta = len(contas_correntes) + 1
#     conta = {
#         "agencia": agencia,
#         "numero_conta": numero_conta,
#         "usuario": usuario
#     }
#     contas_correntes.append(conta)
#     print(f"Conta criada com sucesso! Agência: {agencia}, Conta: {numero_conta}")


# def listar_contas():
#     for conta in contas_correntes:
#         print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Titular: {conta['usuario']['nome']}")


# while True:
#     menu()
#     opcao = input("Escolha uma opção: ")

#     if opcao == "1":
#         valor = float(input("Informe o valor do depósito: "))
#         saldo, extrato = deposito(saldo, valor, extrato)

#     elif opcao == "2":
#         valor = float(input("Informe o valor do saque: "))
#         saldo, extrato, numero_saques = saque(
#             saldo=saldo,
#             valor=valor,
#             extrato=extrato,
#             limite=500,
#             numero_saques=numero_saques,
#             limite_saques=3
#         )

#     elif opcao == "3":
#         op_extrato(saldo, extrato=extrato)

#     elif opcao == "4":
#         nome = input("Nome completo: ")
#         data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
#         cpf = input("CPF (somente números): ")
#         endereco = input("Endereço (logradouro, número - bairro - cidade/UF): ")
#         novo_usuario(nome, data_nascimento, cpf, endereco)

#     elif opcao == "5":
#         cpf = input("Informe o CPF do usuário: ")
#         usuario = encontrar_usuario(cpf)
#         if usuario:
#             nova_conta_corrente(usuario)
#         else:
#             print("Usuário não encontrado. Conta não criada.")

#     elif opcao == "6":
#         listar_contas()

#     elif opcao == "0":
#         print("Obrigado por usar o Banco SantANDRÉ. Até logo!")
#         break

#     else:
#         print("Opção inválida. Tente novamente.")
