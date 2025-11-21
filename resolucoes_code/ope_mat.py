# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
operacao = input("Insira a operação que deseja efetuar: (+, -, *, /): ") 

if operacao == '+':
        print(num1 + num2)
elif operacao == '-':
        print(abs(num1 - num2))
elif operacao  == '*':
        print(num1 * num2)
elif operacao == '/':
    print(num1 / num2)
else: print("Operação inválida.")