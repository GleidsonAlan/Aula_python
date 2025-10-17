import os
os.system ('cls')

idade = int(input("Digite sua idade:"))
altura = float(input("Digite sua altura: "))

if(idade >= 16 and idade <=18 and altura >= 1.75 and altura <=1.80):
    print("Aprovada")

else:
    print("Reprovada")    