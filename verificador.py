"""
Este programa vai solicitar ao usuário um número e fara uma serie de calculos, baseado em condicionais:
se o número é par ou impar

se o número for positivo:
    irá calcular:
        raiz quadrada;
        eleva o número ao quadrado;

se o número for negativo:
    irá calcular:
        eleva ao quadrado;


"""

num = float(input("Digite um número: "))

if num %2 == 0:
    print(f"{num} é um número par.")
else:
    print(f"{num} é um número impar")

if num >= 0:
    print("O número que você digitou é positivo")
    raiz_quadrada = num ** 0.5
    print(f"{raiz_quadrada} é a raiz quadrada de {num}")
    qua = num ** 2
    print(f"{qua} é o quadrado de {num}")
else:
    print("O número que você digitou é negativo")
    qua = num ** 2
    print(f"{qua} é o quadrado de {num}")
