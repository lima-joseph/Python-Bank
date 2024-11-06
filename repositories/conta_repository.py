import sqlite3
from models.conta import Conta

class ContaRepository:
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.cursor = self.conexao.cursor()

    def adicionar_conta(self, conta):
        try:
            self.cursor.execute("INSERT INTO contas (numero, titular, saldo) VALUES (?, ?, ?)",
                                (conta.numero, conta.titular, conta.saldo))
            self.conexao.commit()
            print("Conta criada com sucesso!")
        except sqlite3.IntegrityError:
            print("Erro: O número de conta já existe.")

    def buscar_conta(self, numero):
        self.cursor.execute("SELECT numero, titular, saldo FROM contas WHERE numero = ?", (numero,))
        resultado = self.cursor.fetchone()
        return Conta(*resultado) if resultado else None

    def atualizar_saldo(self, numero, saldo):
        self.cursor.execute("UPDATE contas SET saldo = ? WHERE numero = ?", (saldo, numero))
        self.conexao.commit()

    def adicionar_transacao(self, numero_conta, transacao):
        self.cursor.execute("INSERT INTO transacoes (numero_conta, tipo, valor) VALUES (?, ?, ?)",
                            (numero_conta, transacao.tipo, transacao.valor))
        self.conexao.commit()

    def listar_transacoes(self, numero_conta):
        self.cursor.execute("SELECT tipo, valor, data FROM transacoes WHERE numero_conta = ? ORDER BY data DESC",
                            (numero_conta,))
        return self.cursor.fetchall()
