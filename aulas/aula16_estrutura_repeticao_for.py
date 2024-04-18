texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()  #adiciona uma quebra de linha
    print("Executa no final do laço")


# exemplo utilizando a funcão built-in range, 
# onde 0 é a posicão inicial
# o numéro 51 é até onde o for irá percorrer
# e o 5 se trata de incremento, onde ao final de cada volta do for, será somado 5 ao valor atual // i++
for numero in range(0,51,5):
    print(numero, end=" ")


