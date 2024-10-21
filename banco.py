menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
  opcao = input(menu)
  print(opcao)
  if opcao == 'd':
    valor = float(input('Informe o valor do depósito: '))
    if valor > 0:
      saldo = saldo + valor
      extrato = extrato + f'Depósito R$ {valor:.2f}\n'
    else:
      print('Operação falhou! O valor informado é inválido')  
  elif opcao == 's':
    valor_saque = float(input('Informe o valor do saque: '))
    if saldo > valor_saque and numero_saques <= LIMITE_SAQUES and valor_saque <= limite:
       saldo = saldo - valor_saque
       numero_saques += 1
  elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
  elif opcao == 'q':
     break
  else:
     print('Opção escolhida é inválida')

    
