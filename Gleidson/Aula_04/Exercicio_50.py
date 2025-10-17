import os
os.system('cls')
import math 

base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

perimetro = 2 * (base + altura)

area = base * altura

diagonal = (base + altura) 

print(f"Perímetro: {perimetro}")
print(f"Área: {area}")
print(f"Diagonal: {diagonal}")