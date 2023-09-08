"""
Escribir un programa que permita ingresar tres números enteros e indicar cual
es el mayor.
"""
num1 = input("ingrese un numero: ")
num2 = input("ingrese un numero: ")
num3 = input("ingrese un numero: ")

if num1 > num2 and num1 > num3:
    print(f"{num1} es el mayor")
elif num2 > num3 and num2 > num1:
    print(f"{num2} es el mayor")
elif num3 > num1 and num3 > num2:
    print(f"{num3} es el mayor ")
