from controllers.conta_controller import ContaController

def menu():
    controller = ContaController()
    
    while True:
        print("\n--- Menu Banco ---")
        print("1. Criar Conta")
        print("2. Exibir Saldo")
        print("3. Realizar Transação")
        print("4. Exibir Transações")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            numero = input("Digite o número da conta: ")
            titular = input("Digite o nome do titular: ")
            controller.criar_conta(numero, titular)
        
        elif opcao == '2':
            numero = input("Digite o número da conta: ")
            controller.exibir_saldo(numero)
        
        elif opcao == '3':
            numero = input("Digite o número da conta: ")
            tipo = input("Digite o tipo de transação (depósito/saque): ").lower()
            valor = float(input("Digite o valor da transação: "))
            controller.realizar_transacao(numero, tipo, valor)
        
        elif opcao == '4':
            numero = input("Digite o número da conta: ")
            controller.exibir_transacoes(numero)
        
        elif opcao == '5':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")
