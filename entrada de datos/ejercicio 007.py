# Escribir un programa que permita ingresar un número entero. Debe mostrarse el número ingresado:
# a. Multiplicado por 10. (utilizar el operador *) a. Dividido por 10. (utilizar el operador /) a.
# Elevado al cuadrado. (utilizar el operador **)
# Cada resultado debe mostrarse en una línea distinta
numero = int(input("ingrese un numero: "))

print(f"""
{numero} * 10 = {numero*10}
{numero} / 10 = {numero/10}
{numero} ** 2 = {numero ** 2} 
""")