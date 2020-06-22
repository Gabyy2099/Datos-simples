# Escribir un programa que lea un entero 'n' positivo ingresado por el usuario
# Luego mostrar en pantalla la suma de todos los enteros de 1 hasta el 'n'

# Codigo:
n = int(input('Ingrese un numero entero: '))
sum = n * (n+1)//2
print('La suma de todos los numeros enteros hasta ,', n, ' es:', sum)
