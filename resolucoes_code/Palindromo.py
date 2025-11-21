# Verificando se uma palavra é palindromo

palavra = input("Insira uma palavra para que seja verificado se ela é um não um palíndromo: ").lower()

if palavra == palavra[::-1]:
    print("A palavra", palavra, "é um palíndromo!")
else:
    print("A palavra", palavra, "não é um palíndromo")

