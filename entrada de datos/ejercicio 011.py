"""
Escribir un programa que permita resolver el siguiente problema:

Tres personas aportan diferente capital a una sociedad y desean saber el valor total aportado y qué porcentaje
aportó cada una (indicando nombre y porcentaje).

Solicitar la carga por teclado del nombre de cada socio y su capital aportado, a partir de esto calcular e 
informar lo requerido previamente
"""
nombre_persona1=input("ingrese su nombre: ")
persona1 = int(input("ingrese capital aportado: "))
nombre_persona2=input("ingrese su nombre: ")
persona2 = int(input("ingrese capital aportado: "))
nombre_persona3=input("ingrese su nombre: ")
persona3 = int(input("ingrese capital aportado: "))

total = persona1 + persona2 + persona3

porcentaje_persona1=(persona1*100)/total
porcentaje_persona2=(persona2*100)/total
porcentaje_persona3=(persona3*100)/total
print(f"""
{nombre_persona1} aporto el %{porcentaje_persona1}
{nombre_persona2} aporto el %{porcentaje_persona3}
{nombre_persona3} aporto el %{porcentaje_persona3}
""")