import os
os.system('cls')

numero = int(input("Digite um numero:  "))

if(numero > 20):
    print(f"numero{numero}, maior do que 20")

elif(numero == 20):
    print(f"numero{numero}, igual a 20")

else:
   print(f"numero{numero} menor que 20")