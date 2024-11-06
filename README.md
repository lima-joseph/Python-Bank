## Como Rodar o Projeto

#### 1. Clone o repositório ou faça o download do código-fonte.
#### 2. Navegue até o diretório onde os arquivos do projeto estão localizados.
#### 3. Execute o script `main.py`:

  ```bash
  python main.py
```

**O sistema exibirá um menu interativo onde você pode:**
- Criar uma nova conta.
- Exibir o saldo de uma conta.
- Realizar transações de depósito ou saque.
- Ver o histórico de transações de uma conta.

- Exemplo de Execução
Quando o sistema for executado, você verá um menu como este:

```markdown
--- Menu Banco ---
1. Criar Conta
2. Exibir Saldo
3. Realizar Transação
4. Exibir Transações
5. Sair
```

**Escolha uma opção:**
- `Criar Conta:` Você será solicitado a informar o número da conta e o nome do titular.
- `Exibir Saldo:` O saldo da conta será mostrado.
- `Realizar Transação:` Você pode realizar um depósito ou saque e o sistema fará a validação do tipo de transação.
- `Exibir Transações:` O histórico de transações será mostrado.

**Funcionalidades Futuras**
- `Autenticação de Usuário:` Implementar autenticação para garantir que as transações sejam feitas apenas por titulares de contas.
- `Persistência em Banco de Dados:` Substituir o armazenamento em memória por um banco de dados real (MySQL, SQLite, etc.).
- `Interface Gráfica:` Desenvolver uma interface gráfica utilizando frameworks como Tkinter ou PyQt.
