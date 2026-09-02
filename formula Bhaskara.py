import os
import math

os.system("cls")

a = float(input("digite o valor a: "))
b = float(input("digite o valor b: "))
c = float(input("digite o valor c: "))

if a == 0:
    print("valor de 'a' não pode ser zero em equação de 2º grau")
else:
    delta = (b ** 2) - (4 * a * c)
    print(f"delta = {delta}")

    if delta < 0:
        print("a equação não possui raiz real")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"a equação possui uma raiz real: {x}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")