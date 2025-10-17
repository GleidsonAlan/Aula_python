import math
import os
os.system ('cls')


nome = input("Digite seu nome: ")

if(nome[:4].upper() in ["josé", "Jose"]):
    print(nome)

else:
    print("não comeca com 'jose' ")
