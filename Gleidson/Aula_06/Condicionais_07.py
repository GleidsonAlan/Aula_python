import os
os.system ('cls')

nota_01 = 5
nota_02 = 6
nota_03 = 9
nota_04 = 7 

media = (nota_01+nota_02+nota_03+nota_04) / 4

if( media >=7):
    print(f"{media}, Aprovado")

elif(media >= 5 and media < 7 ):
    print(f"{media},Aluno de recuperação!") 

else:
    print(f"{media},Reprovado")    