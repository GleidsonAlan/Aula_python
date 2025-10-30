#lendo numeros inteiros e informar o sucessor e antecessor 
import os
os.system ('cls')

valor = int(input("Digite o seu numero:"))

sucessor = valor + 1
antecessor = valor - 1

print(f"Seu numero é :{valor}, o sucessor é {sucessor}, e o antecessor é {antecessor}")