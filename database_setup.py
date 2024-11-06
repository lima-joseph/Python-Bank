import sqlite3

def inicializar_banco():
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS contas (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      numero TEXT UNIQUE,
                      titular TEXT,
                      saldo REAL DEFAULT 0.0)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS transacoes (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      numero_conta TEXT,
                      tipo TEXT,
                      valor REAL,
                      data TEXT DEFAULT (datetime('now', 'localtime')),
                      FOREIGN KEY (numero_conta) REFERENCES contas (numero))''')
    
    conexao.commit()
    conexao.close()

inicializar_banco()
