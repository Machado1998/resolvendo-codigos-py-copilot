# Dando a média das notas iseridas pelo usuário

quantidade = int(input("Qual a quantidade de notas que serão inseridas: "))

soma = 0

for q in range(quantidade):
    nota = float(input(f"Nota {q+1}: "))
    soma += nota

media = soma / quantidade
print("Média =", media)