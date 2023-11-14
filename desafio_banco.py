menu = """  
               ==========================
                    (1) Deposito 
                    (2) Saque
                    (3) Extrato 
                    (X) Sair  
               ===========================

               Qual operação você deseja realizar? :  """

saldo = 0
limite_diario = 500
extrato = ""
numero_saques = 0 
LIMITE_SAQUES = 3

while True:

     opcao = input(menu)

     if opcao == "1":

          print("               ======= Deposito ======= \n")
          valor = float(input("\n Qual o valor voce quer depositar? : " ))
          
          if valor > 0:
               saldo += valor
               extrato += f"Depósito: R$ {valor:.2f}\n"
          else:
               print("Valor depositado é invalido")

     elif opcao == "2":
     
          print("\n               ======= Saque =======\n")
          valor = float(input("\n Qual o valor voce quer sacar? :" ))

          if valor> 0:
               
               excede_limite_diario = valor > limite_diario

               excede_limite_saque = numero_saques >= LIMITE_SAQUES

               excede_saldo = valor > saldo
               

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

          

     elif opcao == "3":

          print("\n              ======= Extrato =======\n")
          print(extrato)
          print(f"Saldo: R$ {saldo:.2f}\n")

     elif opcao == "4":
     
          print("\n              ======= Obrigado pela sua confiança. Até a próxima ! =======\n")
          break
