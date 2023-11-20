def menu():
    menu = """\n                          MENU
               ==========================
                    (1) Deposito 
                    (2) Saque
                    (3) Extrato
                    (4) Criar Usuario
                    (5) Criar Nova Conta
                    (6) Listar Contas
                    (S) Sair  
               ===========================

                "Qual operação você deseja realizar? : """
    return input(menu)

def deposito(saldo, valor, extrato, /):
          
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Valor depositado é invalido")

    return saldo, extrato



def saque(*, saldo, valor, extrato, limite_diario, numero_saques, LIMITE_SAQUES):

    excede_limite_diario = valor > limite_diario
    excede_limite_saque = numero_saques >= LIMITE_SAQUES
    excede_saldo = valor > saldo

    if valor> 0:
               
        if excede_limite_diario:

            print ("O seu limite para saque é de R$ 500.00")

        elif excede_saldo:

            print ("Saldo insuficiente")

        elif excede_limite_saque:

            print ("Você atingiu o seu limite diário de saques.")

        elif valor > 0:

            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
    else:

        print ("Operação inválida")

    return saldo, extrato


def exibir_extrato(saldo, / , *, extrato):
    
    print("\n              ======= Extrato =======\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}\n")


def criar_usuario(usuarios):
    repeat = ""
    cpf = input("Digite o seu CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        
        repeat = input('\n Já existe usuário com esse CPF. Digite "M" para voltar ao menu principal ou "R" para tentar tovamente!')
        
        if repeat.lower() == "m":
            return

        else:
            return criar_usuario(usuarios)

    nome = input("Digite o seu nome completo:")
    data_nascimento = ("Digite sua data de Nacimento (mm-dd-aaaa")
    endereco = input("Digite o seu endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    repeat2 = ""
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
            repeat2 = input('\n Usuário inesitente. Digite "C" para voltar ao menu principal ou "R" para tentar tovamente!')
        
            if repeat2.lower() == "c":
                return 

            else:
                return criar_conta(agencia, numero_conta, usuarios)


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 80)
        print(linha)


def sair():
    
    print("\n              ======= Obrigado pela sua confiança. Até a próxima ! =======\n")
    



    


def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite_diario = 500
    extrato = ""
    numero_saques = 0 
    
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "1":

            print("               ======= Deposito ======= \n")
            valor = float(input("\n Qual o valor voce quer depositar? : " ))
            saldo, extrato = deposito(saldo, valor, extrato)
            

        elif opcao == "2":

            print("\n               ======= Saque =======\n")
            valor = float(input("\n Qual o valor voce quer sacar? :" ))
            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite_diario=limite_diario,
                numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES,
                )
             
            
          
        elif opcao == "3":

            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":

            criar_usuario(usuarios)

        elif opcao == "5":

            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "6":
     
            listar_contas(contas)

        elif opcao == "S":
     
            sair()
            break

main()