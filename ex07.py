custo_de_fabrica = float(input("Informe o custo de fabrica: "))
distribuidor =  custo_de_fabrica  * 0.28
impostos = custo_de_fabrica  * 0.45
custo_total = custo_de_fabrica + distribuidor + impostos
print(f"{custo_total}")
