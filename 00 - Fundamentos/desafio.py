def depositar(saldo, valor, extrato, /):
    try:
        if valor <= 0:
            print('Valor insuficiente para depositar.')
        else:
            saldo += valor
            extrato += f'Entrada: R$ {valor:.2f}\n'
            print(f'Deposito de R$ {valor:.2f} realizado com sucesso.')

    except ValueError:
        print('Erro... Digite apenas numeros.')

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    try:
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if valor <= 0:
            print('Operacao invalida. Valor invalido.')
        elif excedeu_saldo:
            print('Operacao invalida. Saldo insuficiente.')
        elif excedeu_limite:
            print(f'Operacao invalida. Valor de saque excedeu o limite de R$ {limite:.2f}.')
        elif excedeu_saques:
            print('Operacao invalida. Numero maximo de saques diarios excedido.')
        else:
            saldo -= valor
            numero_saques += 1
            extrato += f'Saida: R$ {valor:.2f}\n'
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')

    except ValueError:
        print('Erro... Digite apenas numeros.')

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print('--- Extrato ---')
    print('Nao foram realizadas movimentacoes.' if not extrato else extrato)
    print(f'Saldo atual: R$ {saldo:.2f}')

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente['cpf'] == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def criar_cliente(clientes):
    nome = input('Nome completo: ')
    data_nascimento = input('Data de nascimento (DD/MM/AAAA): ')

    cpf = input('CPF (somente numeros ou com pontuacao): ')

    if len(cpf) != 11:
        print('Erro... CPF invalido. Digite 11 digitos.')
        return clientes

    if filtrar_cliente(cpf, clientes):
        print('Erro... Ja existe um cliente cadastrado com esse CPF.')
        return clientes

    logradouro = input('Logradouro: ')
    bairro = input('Bairro: ')
    cidade = input('Cidade: ')
    sigla_estado = input('Sigla do estado (ex: SP, RJ): ').upper()

    endereco = f'{logradouro} - {bairro} - {cidade}/{sigla_estado}'

    cliente = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco,
    }

    clientes.append(cliente)
    print(f'Cliente {nome} cadastrado com sucesso!')
    return clientes


def criar_conta(numero_conta, clientes, contas):
    cpf = input('CPF do cliente (somente numeros ou com pontuacao): ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('Erro... Cliente nao encontrado. Cadastre o cliente antes de criar uma conta.')
        return contas

    conta = {
        'agencia': '0001',
        'numero_conta': numero_conta,
        'cliente': cliente,
    }

    contas.append(conta)
    print(f'Conta corrente criada com sucesso!')
    print(f'Agencia: 0001 | Conta: {numero_conta} | Titular: {cliente["nome"]}')
    return contas


def sistema_bancario():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    clientes = []
    contas = []

    while True:
        menu = [
            'Depositar',
            'Sacar',
            'Extrato',
            'Novo Cliente',
            'Nova Conta',
            'Sair'
        ]
        print('-' * 30)
        print('--- Sistema Bancario ---')
        for i, opcao in enumerate(menu, start=1):
            print(f'{i} - {opcao}')
        print('-' * 30)
        print('Escolha uma das opcoes:')

        try:
            escolha = int(input('> '))
        except ValueError:
            print('Erro... Digite apenas numeros.')
            continue

        if escolha == 1:
            try:
                valor = float(input('Valor de deposito:\n'))
            except ValueError:
                print('Erro... Digite apenas numeros.')
                continue
            saldo, extrato = depositar(saldo, valor, extrato)

        elif escolha == 2:
            try:
                valor = float(input('Valor de saque:\n'))
            except ValueError:
                print('Erro... Digite apenas numeros.')
                continue
            extrato_anterior = extrato
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )
            if extrato != extrato_anterior:
                numero_saques += 1

        elif escolha == 3:
            exibir_extrato(saldo, extrato=extrato)

        elif escolha == 4:
            clientes = criar_cliente(clientes)

        elif escolha == 5:
            numero_conta = len(contas) + 1
            contas = criar_conta(numero_conta, clientes, contas)

        elif escolha == 6:
            print('Saindo do sistema...')
            break

        else:
            print('Operacao invalida, por favor selecione novamente a operacao desejada.')

sistema_bancario()