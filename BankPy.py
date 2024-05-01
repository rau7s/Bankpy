saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
    else:
        print('Valor do depósito deve ser positivo.')

def sacar(valor):
    global saldo, extrato, numero_saques
    if valor <= saldo and valor <= limite_saque and numero_saques < LIMITE_SAQUES:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
    else:
        if valor > saldo:
            print('Saldo insuficiente para saque.')
        elif valor > limite_saque:
            print(f'Limite máximo de saque é de R$ {limite_saque:.2f}.')
        else:
            print('Número máximo de saques diários atingido.')

def exibir_extrato():
    global extrato, saldo
    print('Extrato:')
    if extrato:
        print(extrato)
    else:
        print('Nenhuma transação realizada ainda.')
    print(f'Saldo atual: R$ {saldo:.2f}')

# Loop principal do programa
while True:
    print("\nMENU:")
    print("[d] Depositar")
    print("[s] Sacar")
    print("[e] Extrato")
    print("[q] Sair")

    opcao = input("=> ").strip().lower()

    if opcao == "d":
        valor = float(input("Digite o valor do depósito: "))
        depositar(valor)
    elif opcao == "s":
        valor = float(input("Digite o valor do saque: "))
        sacar(valor)
    elif opcao == "e":
        exibir_extrato()
    elif opcao == "q":
        print("Saindo...")
        break
    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")