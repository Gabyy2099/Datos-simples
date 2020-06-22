# Escribir un programa que pida al usuario dos números enteros ('n' y 'm')
# mostrar por pantalla 'n' entre 'm' da un cociente 'c' y de resto 'r'

# Codigo:
n = int(input('Ingrese el primer numero entero:'))
m = int(input('Ingrese el segundo numero entero:'))
c = n/m
r = n%m
print(n,' entre ', m, ' da un cociente', c, ' y de resto ', r)
