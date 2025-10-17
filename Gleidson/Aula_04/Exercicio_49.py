import os
os.system('cls')

nome = str(input("Digite seu nome: "))

print(f"Todos o nome: {nome}")
print(f"Primeiro caracter: {nome[0]}")
print(f"Ultimo caracter: {nome[-1]}")
print(f"Primerio até o terceiro: {nome[:3]}")
print(f"Quarto caracter: {nome[3]}")
print(f"Todos menos o primeiro: {nome[1:]}")
print(f"Os dois ultimos: {nome[-2:]}")