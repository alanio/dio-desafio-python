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

	if opcao == "d":
		print("Depósito")
		
		valor_deposito = float(input("Digite o valor do depósito: "))
		if valor_deposito > 0:
			saldo += valor_deposito
			acao = f"Deposito realizado no valor de {valor_deposito:.2f}!\n"
			extrato += acao
			print(acao)
		else:
			print("Operação inválida")

	elif opcao == "s":
		print("Sacar")
		if numero_saques < LIMITE_SAQUES:
			saque = float(input("informe o valor do saque: "))
			if saque <= limite:
				if saque <= saldo:
					saldo -= saque
					acao = f"Saque realizado no valor de {saque:.2f}!\n"
					extrato += acao 
					print(acao)
					numero_saques += 1
				else:
					print("Saldo insuficiente!")
			else:
				print("Saque não realizado, excede limite diário!")
		else:
			print("Quantidade de saque diário atingido!")

	elif opcao == "e":
		print("Extrato")
		if extrato == "":
			print("Não foram realizadas movimentações.")
		else:
			print(extrato)
			print(f"Saldo: R$ {saldo:.2f}")

	elif opcao == "q":
		break

	else:
		print("Operação inválida, por favor selecione novamente a operação desejada.")