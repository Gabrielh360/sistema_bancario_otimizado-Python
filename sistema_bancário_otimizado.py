import textwrap

def menu():
    menu = """\n
    ---------------- MENU ----------------
    [1] Depositar 🏧
    [2] Sacar 💳
    [3] Extrato 📋
    [4] Transferência 💸
    [5] Criar Nova Conta 📲
    [6] Listar Contas 📜
    [7] Novo Usuário 🙋‍♂️
    [0] Sair 👋
 
    => """

    return input(textwrap.dedent(menu))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    LIMITE_TRANSFERENCIA = 10000000

    saldo = 0
    limite = 500
    pessoa = ""
    extrato = ""
    transferir = saldo
    numero_saques = 0
    numero_transferencias = 0
    contas = []
    usuarios = []


    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
            

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor, 
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

            
        elif opcao == "3":
            exebir_extrato(saldo, extrato=extrato)
            

        elif opcao == "4":
            valor = float(input("Informe o valor da transferência: "))
            pessoa = input("Informe pra quem ira traferir o valor: ")

            saldo, extrato = transferencia(
                saldo=saldo, 
                valor=valor, 
                extrato=extrato,
                limite=limite,
            )


        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)


        elif opcao == "6":
            listar_contas(contas)


        elif opcao == "7":
            criar_usuario(usuarios)


        elif opcao == "0":
            print("\n Obrigado por usar nosso sistema bancário, volte sempre! 👋 \n")
            break

        else:
            print("\n❌ Operação inválida, por favor selecione novamente a operação desejada.")



def depositar(saldo, valor, extrato, /):
    if valor > 0:
                print("\n✅ Depósito realizado com sucesso!")
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("\n❌ Operação falhou! O valor informado é inválido.")

    return saldo, extrato
    

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n❌ Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("\n❌ Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("\n❌ Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        print("\n✅ Saque realizado com sucesso!")
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("\n❌ Operação falhou! O valor informado é inválido.")
        
    return saldo, extrato


def exebir_extrato(saldo, /, *, extrato):
    print("\n----------------- 📋 EXTRATO 📋 -----------------")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("-------------------------------------------------")


def transferencia(*, saldo, valor, extrato, limite):
    excedeu_saldo = valor > saldo

    excedeu_limite_transferencia = valor > limite

    if excedeu_saldo:
            print("\n❌ Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite_transferencia:
            print("\n❌ Operação falhou! O valor da transferência excede o limite.")

    elif valor > 0:
        print("""
                  ✅ Transferência realizada com sucesso!""")
        saldo -= valor
        extrato += f"Transferência: R$ {valor:.2f}\n"

    else:
        print("\n❌ Operação falhou! O valor informado é inválido.""")
       
    return saldo, extrato


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n ✅ Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario":usuario}

    print("\n❌ Usuário não encontrado, fluxo de criação de conta encerrado!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """

        print("-" * 100)
        print(textwrap.dedent(linha))


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n❌ Já existe um usuário com esse CPF!")
        return
    
    nome = input("Informe o Nome Completo: ")
    data_nascimento = input("Informe a Data de Nascimento (DD-MM-AAAA): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\n ✅ Usuário criado com sucesso!")

main()

