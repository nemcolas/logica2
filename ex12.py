comprimento = float(input("Informe o comprimento da cozinha: "))
largura = float(input("Informe o largura da cozinha: "))
altura = float(input("Informe o altura da cozinha: "))

area1 = comprimento * altura * 2
area2 = largura * altura * 2

areatotal = area1 + area2

qtdcaixas = areatotal / 1.5

print(f"a area total dessa cozinha é de {areatotal}m2, dessa forma, é necessario {qtdcaixas:.0f} de caixas de azuleijo")

