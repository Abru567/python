# Escribir un programa que permita ingresar valores del mismo tipo para las variables num1 y num2.
# Una vez cargadas, mostrar ambas variables por pantalla, intercambiá sus valores
# (que lo cargado en num1 quede en num2, y viceversa) y volvé a mostrarlas actualizadas.
# Como pensarlo:
# -Pedir al usuario que ingrese un valor para la variable num1.
# -Pedir al usuario que ingrese un valor para la variable num2.
# -Mostrar por pantalla el valor de las variables num1 y num2.
# -Intercambiar los valores de las variables num1 y num2.
# -Mostrar por pantalla el valor de las variables num1 y num2.
num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese un numero: "))
print(f"""num1 = {num1}
num2 = {num2}""")
num1 = num2 + num1
num2 = num1 - num2
num1 = num1 - num2
print(f"""num1 = {num1}
num2 = {num2}""")