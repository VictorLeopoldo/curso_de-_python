"""
Este programa irá solicitar ao usuário que digite dois números e
verifique qual deles é o maior

This program will ask the user to input two numbers and check which
one is greater.
"""
num = float(input("Digite  o primeiro número: "))
num1 = float(input("Digite  o segundo número: "))

if num == num1:
    print("Os números são iguais")
elif num < num1:
    print("O número: ", num1, "é o maior")
else:
    print("O número: ", num, "é o maior")
