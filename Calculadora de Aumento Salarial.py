import os
os.system("cls")

salario =float(input("digite seu salario atual:"))

if salario > 2000:
    novo_salario = salario * 1.10
    aumento = "10%"
else:
    novo_salario = salario * 1.15
    aumento = "15%"


    print(f"aumenro aplicado: {aumento}")
    print(f"seu salario é {novo_salario: .2f}")