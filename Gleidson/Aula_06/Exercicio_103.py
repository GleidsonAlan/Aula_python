import os
os.system('cls')

ano = int(input("Digite o ano do seu nasccimento: "))
anoAtual = int(input("Digite o ano atual: "))

if(anoAtual - ano != 0 and anoAtual-ano <= 100):
    idade = anoAtual-ano
    print(f"idade {idade}")

else:
    print("Data invalida")   