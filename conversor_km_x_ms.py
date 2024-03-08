"""
Este programa irá converter km/h em m/s
This program will convert km/h for m/s
"""

"""
Imprime a informação para o usuário
Print a information for user
"""
print("Conversor de km/h para m/s\n")

"""
Solicita ao usuário a informação
Prompts the user for information
"""
km = float(input("Informe a velocidade em km/h:\n"))

ms = km/3.6
"""
Imprime a informação para o usuário
Print a information for user
"""
print("A velocidade de: ", km, "km/h", "equivale a:\n ", ms, "m/s")
