"""
Definición del problema: Una inmobiliaria paga a sus vendedores un salario base, más una comisión fija por 
cada venta realizada, más el 5% del valor de esas ventas. Realizar un programa que imprima el nombre del 
vendedor y el salario que le corresponde en un determinado mes.
Se leen por teclado el nombre del vendedor, la cantidad de ventas que realizó y el valor total de las mismas.
¿Sobran datos? ¿Qué datos sobran?
"""
nombre = input("Ingrese el nombre del empleado: ")
cantidad_de_ventas = int(input("Ingrese la cantidad de ventas realizadas: "))
valor_de_ventas = int(input("ingrese el valor de las ventas: "))
comision_fija = 500
salario_base = 5000
valor_total_por_comision_ventas = comision_fija * cantidad_de_ventas
valor_total_de_ventas = cantidad_de_ventas * (valor_de_ventas * 0.05)
salario_total = salario_base + valor_de_ventas + valor_total_de_ventas

print(f"""
----------------------------------------
Nombre: {nombre}
----------------------------------------
Salario base:            ${salario_base}
Ventas:                  ${valor_total_de_ventas}
Comision por ventas:     ${valor_total_por_comision_ventas}
----------------------------------------
SubTotal:                ${salario_total}
Total:                   ${salario_total}
----------------------------------------
""")