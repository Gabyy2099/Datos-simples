# En este programa se intenta preguntar el nombre del usuario en la consola y un número entero
# luego mostrar en pantalla  en líneas distintas el nombre del usuario tantas veces como el número introducido

# Codigo:
nom = input('Ingrese el nombre de usuario:')
num = int(input('Ingrese un numero: '))
print((nom + str('\n')) * num)
