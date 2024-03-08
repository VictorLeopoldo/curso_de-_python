"""
Este programa irá converter uma temperatura de graus Farenheit para
graus Celsius

This program will convert a temperature from degrees Farenheit to degrees Celsius
"""
"Imprime a informação para o usuário"
"Print the information for the user"
print("Este programa faz a conversão de temperatura de Fº para Cº")

"Solicita ao usuário o valor da temperatura"
"Prompts the user for temperature value"
tem = float(input("Digite a temperatura em Farenheit para conversão: "))

"Realiza o calculo"
"Perform the calculation"
c = 5.0*(tem -32.0)/9.0

"Imprime a informação para o usuário"
"Print the information for the user"
print("A temperatura que você solicitou a conversão foi: , ", tem)


"Imprime o resultado para o usuário"
"Print the result for the user"
print("O valor dela em Celsius é: ", c)
