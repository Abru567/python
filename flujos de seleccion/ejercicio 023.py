"""
Escribir un programa que permita ingresar tres números enteros y mostrar el mayor
el menor y el valor que esta en medio.

Ejemplo: Si se ingresan los números 5, 3 y 7, el programa debe mostrar el número 
5 como el menor, el número 7 como el mayor y el número 3 como el que esta en 
medio.

Otra vez se mezclaron las instrucciones, ¿podrías arreglarlas?

numero_uno = int(input("Ingrese el primer número: "))
numero_dos = int(input("Ingrese el segundo número: "))
numero_tres = int(input("Ingrese el tercer número: "))
if medio < menor:
auxiliar = medio
medio = menor
menor = auxiliar
if numero_tres > mayor:
mayor = numero_tres
medio = numero_uno
menor = numero_dos
if numero_dos > mayor:
mayor = numero_dos
medio = numero_uno
menor = numero_tres
mayor = numero_uno
medio = numero_dos
menor = numero_tres
print("El mayor es: ", mayor)
print("El medio es: ", medio)
print("El menor es: ", menor)
"""
numero_uno = int(input("Ingrese el primer número: "))
numero_dos = int(input("Ingrese el segundo número: "))
numero_tres = int(input("Ingrese el tercer número: "))
mayor =0
medio = 0
menor=0
if numero_uno < numero_dos  and numero_uno < numero_tres:
    menor = numero_uno
elif numero_uno > numero_dos  and numero_uno > numero_tres:
    mayor = numero_uno
else:
    medio = numero_uno

if numero_dos < numero_uno  and numero_dos < numero_tres:
    menor = numero_dos
elif numero_dos > numero_uno  and numero_dos > numero_tres:
    mayor = numero_dos
else:
    medio = numero_dos


if numero_tres < numero_uno  and numero_tres < numero_dos:
    menor = numero_tres
elif numero_tres > numero_dos  and numero_tres > numero_uno:
    mayor = numero_tres
else:
    medio = numero_tres




print("El mayor es: ", mayor)
print("El medio es: ", medio)
print("El menor es: ", menor)