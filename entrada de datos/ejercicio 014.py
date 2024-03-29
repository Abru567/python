# Escribir un programa que permita al usuario ingresar el ancho y largo de un terreno en metros, junto con el
# valor del metro cuadrado de tierra. El programa debe calcular y mostrar el valor total del terreno. 
# Además, debe calcular la cantidad de metros de alambre necesarios para cercar completamente el terreno 
# a tres alturas distintas.
# Pensando los pasos para resolver el problema:
# -Solicitar al usuario que ingrese el ancho del terreno en metros y almacenarlo en una variable. Solicitar al 
# usuario que ingrese el largo del terreno en metros y almacenarlo en otra variable.
# -Solicitar al usuario que ingrese el valor del metro cuadrado de tierra y almacenarlo en otra variable. 
# -Calcular el valor total del terreno multiplicando el ancho por el largo y luego multiplicando el resultado
# por el valor del metro cuadrado de tierra.
# -Mostrar el valor total del terreno al usuario.
# -Calcular la cantidad de metros de alambre necesarios para cercar el terreno a tres alturas distintas. 
# Por ejemplo, se puede calcular la cantidad de alambre necesaria para cercar a 1 metro de altura, a 2 metros
# de altura y a 3 metros de altura. Para hacerlo, se debe sumar el perímetro del terreno (2 veces el ancho más 
# 2 veces el largo) y luego multiplicarlo por la cantidad de alturas. Mostrar la cantidad de metros de alambre
# necesarios para cercar el terreno a las tres alturas distintas al usuario

ancho_del_terreno = int(input("Ingrese el ancho del terreno: "))
largo_del_terreno = int(input("Ingrese el largo del terreno: "))
valor_del_metro_cuadrado = int(input("Ingrese el valor del metro cuadrado de tierra: "))

valor_total_del_terreno = (ancho_del_terreno * largo_del_terreno) * valor_del_metro_cuadrado
print(f"el valor total del terreno es de ${valor_total_del_terreno}")

perimetro = (ancho_del_terreno * 2) + (largo_del_terreno * 2)
metro_de_alambre1=1
metro_de_alambre2=2
metro_de_alambre3=3
metros_de_alambre1 = perimetro * metro_de_alambre1
metros_de_alambre2 = perimetro * metro_de_alambre2
metros_de_alambre3 = perimetro * metro_de_alambre3

print(f"""
Cantidad de metros de alambre a usar por metro de altura:
1 metro  de altura = {metros_de_alambre1}m
2 metros de altura = {metros_de_alambre2}m
3 metros de altura = {metros_de_alambre3}m
""")