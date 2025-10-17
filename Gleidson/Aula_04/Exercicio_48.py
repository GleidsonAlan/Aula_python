import math
import os
os.system('cls')

salario = float(input("Digite o seu salario:" ))
quilowatts = float(input("Digite seu quilowatts consumido: "))

custo_por_quilowatts = (salario / 7) / 100

custo_total = custo_por_quilowatts * quilowatts

desconto = custo_total - (custo_total * 0.10)

print(f"seu custo total é de {custo_total}, com {desconto}")

