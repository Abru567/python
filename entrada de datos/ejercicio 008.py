# Escribir un programa que permita ingresar el valor monetario de una hora de trabajo y la cantidad de horas
# trabajadas por día, para calcular el salario semanal de un trabajador que trabaja todos los días hábiles 
# y la mitad de las horas del día hábil los sábados, suponiendo que todas las horas tienen el mismo valor."
# Como pensarlo:
# -Pedir al usuario que ingrese el valor monetario de una hora de trabajo y almacenarlo en una variable
# valor_hora.
# -Pedir al usuario que ingrese la cantidad de horas trabajadas por día por el trabajador y almacenarla 
# en una variable horas_trabajadas_por_dia.
# -Calcular el salario diario del trabajador multiplicando valor_hora por horas_trabajadas_por_dia.
# -Calcular el salario semanal del trabajador multiplicando el salario diario por la cantidad de días hábiles
# de la semana. Para esto, puedes utilizar la constante dias_habiles definida como 5.
# -Calcular la cantidad de horas trabajadas por el trabajador el sábado, que es la mitad de la cantidad de 
# horas trabajadas por día hábil. Para esto, se puede utilizar la vaiable horas_sabado definida como 
# horas_trabajadas_por_dia / 2.
# -Calcular el salario del trabajador por las horas trabajadas el sábado multiplicando valor_hora por
# horas_sabado.
# -Sumar el salario semanal con el salario del sábado para obtener el salario total semanal del trabajador.
# -Mostrar el resultado del salario semanal en la pantalla

valor_hora = int(input("ingrese el valor monetario de una hora de trabajo: "))
horas_trabajadas_por_dia = int(input("ingrese la cantidad de horas trabajadas en un día: "))
dias_habiles = 5

salario_diario = valor_hora * horas_trabajadas_por_dia

salario_semanal = salario_diario * dias_habiles

horas_sabado = horas_trabajadas_por_dia / 2

salario_horas_sabado = valor_hora * horas_sabado

salario_total_semanal = salario_semanal + salario_horas_sabado

print(f""" 
---------------------------------------------------------------
salario diario =                       ${salario_diario}
salario semanal =                      ${salario_semanal}
salario del sabado =                   ${salario_horas_sabado}      
---------------------------------------------------------------
salario total =                        ${salario_total_semanal}
---------------------------------------------------------------
""")