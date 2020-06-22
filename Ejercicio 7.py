# Escribir un programa que le pregunte al usuario la cantidad de horas trabajadas
# el costo de una hora y luego mostrar en pantalla el pago correspondiente


# Codigo:
cant_horas = float(input('Ingrese la cantidad de horas trabajadas :'))
cost_hora = float(input('Ingrese el costo de la hora : '))
monto = round(cant_horas * cost_hora, 2)
print('Su pago correspodiente es de: $', monto)
