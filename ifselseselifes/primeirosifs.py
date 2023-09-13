# calculadora

a = float(input("Primeiro número: "))
b = float(input("Segundo número: "))

print("1 - adição")
print("2 - subtração")
print("3 - multiplicação")
print("4 - divisão")
opcao = int(input("Selecione a opção desejada: "))

if opcao ==1:    
    resultado = a + b
    print(f"{resultado}")
elif opcao ==2:
    resultado = a - b
    print(f"{resultado}")
elif opcao ==3:
    resultado = a * b
    print(f"{resultado}") 
elif opcao ==4:
    if b != 0:
        resultado = a / b
        print("f{resultado}")
    else: 
        print("ERRO, NÃO É POSSIVEL DIVIDIR POR 0")
else:
    print("Opção Invalida")




    



