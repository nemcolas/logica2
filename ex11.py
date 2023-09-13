paes = int(input("Quantidade de pães vendidos: "))
broas = int(input("Quantidade de broas vendidas: "))
total = paes * 0.38 + broas * 4.50

poupanca = total * 0.10

print(f"O total de vendas foi: R${total:.2f}, o valor a ser depositado na poupança é de R${poupanca:.2f}")