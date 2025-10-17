import os
os.system('cls')

nome = input("Digite seu nome: ")
sexo = input("Digite o seu sexo: ")
idade = int(input("digite sua idade: "))

sexo = sexo.lower()

if(idade < 25 and sexo =="f"):
    print(f"nome: {nome}\nAceita")
else:
    print("Não aceito")    