def sistema_bancario():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    
    while True:
        menu = [
            'Depositar',
            'Sacar',
            'Extrato',
            'Sair'
        ]
        print('-' * 30)
        print('--- Sistema Bancario ---')
        for i, opcao in enumerate(menu, start=1):
            print(f'{i}-{opcao}')
        print('-' * 30)
        print('Escolha uma das opcoes:')
        try:
            escolha = int(input('> '))
        except ValueError:
            print('Erro... Digite apenas numeros.')
            continue

        if escolha ==  1:
            try:
                valor_deposito = int(input('Valor de deposito:\n'))
                
                if valor_deposito <= 0:
                    print('Valor insuficiente para depositar.')
                else:
                    saldo += valor_deposito
                    extrato += f'Entrada: R$ {valor_deposito:.2f}\n'
                    print(f'Deposito de R$ {valor_deposito} realizado com sucesso.')
            except ValueError:
                print('Erro... Digite apenas numeros.')
                continue
        elif escolha == 2:
            try:
                valor_saque = int(input('Valor de saque:\n'))
                
                excedeu_saldo = valor_saque > saldo
                excedeu_limite = valor_saque > limite
                excedeu_saques = numero_saques >= LIMITE_SAQUES
                
                if valor_saque <= 0:
                    print('Operacao invalida. Valor invalido.')
                elif excedeu_saldo:
                    print('Operacao invalida. Saldo insuficiente.')
                elif excedeu_limite:
                    print(f'Operacao invalida. Valor de saque excedeu o limite de R$ {limite:.2f}.')
                elif excedeu_saques:
                    print('Operacao invalida. Numero maximo de saques diarios excedido.')
                else:
                    saldo -= valor_saque
                    numero_saques += 1
                    extrato += f'Saida: R$ {valor_saque:.2f}\n'
                    print(f'Saque de R$ {valor_saque} realizado com sucesso.')
                    
            except ValueError:
                print('Erro... Digite apenas numeros.')
                continue
            
        elif escolha == 3:
            print('--- Extrato ---')
            print('Nao foram realizadas movimentacoes.' if not extrato else extrato)
            print(f'Saldo atual: R${saldo:.2f}')
        elif escolha == 4:
            print('Saindo do sistema...')
            break
        else:
            print('Operação invalida, por favor selecione novamente a operação desejada.')
sistema_bancario()