"""
Este programa vai solicitar que o usuário informe a temperatura em graus Celsisu e ira converter
para Fahrenheit e imprimir o resultado para o usuário.

This program will prompt the user to input the temperature in degrees Celsius, convert it to
Fahrenheit, and print the result for the user
"""

"Solicita ao usuário a temperatura em graus Celsius"
"Request the temperature from the user in degress Celsius"
tc = float(input("Informe a temperatura em Cº: "))

"Realiza a conversão"
"Perform the conversion"
tf = tc * (9.0/5.0)+32.0

"Imprime o resultado para o usuário"
"Prints the result for the user"
print("A temperatura convertida em Fº é: ", tf)
