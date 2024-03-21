"""
Este programa solicita ao usuário um numero e verifica de ele é positivo ou
negativo, sendo positivo irá calcular a raiz quadrada, se for negatuivo
irá dizer que o número é inválido
"""

num = float(input("Digite um número: "))

if num >= 0:
    raiz_qua = num ** 0.5
    print("A raiz quadrada é: ", raiz_qua)
else:
    print("O número é invalido")
