"""
Este programa solicita duas notas de alunos, verifica
se as notas são validas e exibe na tela a média destas notas.
"""

print("Calculador de média de notas")
print("\n Você deverá informar as duas notas, lembrando que as notas deve ser um valor entre 0 à 10.\n\n")
n1 = float(input("Digite a primeira nota:\n"))
n2 = float(input("Digite a segunda nota:\n "))

if 0 <= n1 <= 10 and 0 <= n2 <= 10:
    media = (n1 + n2 )/ 2
    print(f"A media de {n1} e {n2} é:\n {media}")
else:
    print("Você digitou alguma nota no formato inválido")
