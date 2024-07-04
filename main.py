menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"depósito: R$ {valor: .2f}\n"
            print("Depósito realizado com sucesso")
        else:
            print("valor inválido para depósito")
        

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Saldo Insufiiciente")
        elif excedeu_limite:
            print(f"O limite de R$500 foi ultrapassado em R${valor-500}\n")
        elif excedeu_saques:
            print("O limite de saques diários foi atingido")
        elif valor >0:
            saldo -= valor
            extrato += f"Saque: R$ {valor: .2f}\n"
            numero_saques +=1
            print("Saque realizado, obrigado por escolher o nosso banco \nVolte Sempre!")
        else:
            print("Valor inválido")
        
        
            
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "0":
        break


    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")