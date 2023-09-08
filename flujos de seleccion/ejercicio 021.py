"""
Escribir un programa que permita ingresar dos números enteros e indicar si el 
primero es mayor, menor o igual al segundo.
"""
numero1 = input("ingrese un numero entero: ")
numero2 = input("ingrese un numero entero: ")
if numero1 > numero2:
    print("El primer numero es mayor al segundo")
elif numero1 < numero2:
    print("El primer numero es menor al segundo")
elif numero1 == numero2:
    print("El primer numero es igual al segundo")
