# Escribir un programa que pida al usuario su peso en kg y su estaruta en mts
# Calcular el imc(indice de masa corporal) y almacenarlo en una variable
# luego mostrar por pantalla el imc redondeado con dos decimales

# Codigo:
peso = float(input('Ingrese su peso en kilogramos:'))
alt = float(input('Ingrese su estatura en metros:'))
imc = round(peso/(alt**2), 2)
print('Tu indice de masa corporal es ', imc)
