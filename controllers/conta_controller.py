from models.transacao import Transacao
from models.conta import Conta
from repositories.conta_repository import ContaRepository

class ContaController:
    def __init__(self):
        self.conta_repo = ContaRepository()

    def criar_conta(self, numero, titular):
        if not self.conta_repo.buscar_conta(numero):
            nova_conta = Conta(numero, titular)
            self.conta_repo.adicionar_conta(nova_conta)
        else:
            print("Erro: Conta com esse número já existe.")

    def exibir_saldo(self, numero):
        conta = self.conta_repo.buscar_conta(numero)
        if conta:
            print(f"Saldo atual de {conta.titular}: R$ {conta.saldo:.2f}")
        else:
            print("Erro: Conta não encontrada.")

    def realizar_transacao(self, numero, tipo, valor):
        conta = self.conta_repo.buscar_conta(numero)
        if not conta:
            print("Erro: Conta não encontrada.")
            return

        if tipo not in ["depósito", "saque"]:
            print("Erro: Tipo de transação inválido.")
            return

        if tipo == "depósito":
            novo_saldo = conta.saldo + valor
        elif tipo == "saque":
            if conta.saldo < valor:
                print("Erro: Saldo insuficiente.")
                return
            novo_saldo = conta.saldo - valor

        transacao = Transacao(numero, tipo, valor)
        self.conta_repo.atualizar_saldo(numero, novo_saldo)
        self.conta_repo.adicionar_transacao(numero, transacao)
        print(f"{tipo.capitalize()} de R$ {valor:.2f} realizado com sucesso.")

    def exibir_transacoes(self, numero):
        conta = self.conta_repo.buscar_conta(numero)
        if conta:
            transacoes = self.conta_repo.listar_transacoes(numero)
            if transacoes:
                print("\nHistórico de transações:")
                for tipo, valor, data in transacoes:
                    print(f"{data} - {tipo.capitalize()}: R$ {valor:.2f}")
            else:
                print("Nenhuma transação encontrada.")
        else:
            print("Erro: Conta não encontrada.")
