quantidade_frango = int(input("Digite a quantidade de frangos: "))
pe_direito = 0.40
pe_esquerdo = 0.35 + 0.35
custo_frango = pe_direito + pe_esquerdo
custo_total = quantidade_frango * custo_frango
print(f"o custo total para a granja é de R$:{custo_total:.2f}")

