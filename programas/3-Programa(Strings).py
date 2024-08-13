#Las cadenas de caracteres o mejor como Strings, es una serie de caracteres compuestas por letras, 
# números, signos y símbolos, que dentro de sus funciones destaca la interacción de un programa con el usuario.

#La asignación: consiste en asignar una cadena de caracteres a otra. Operador(+=).

#variables
Mensaje1 = 'Hola'
Mensaje1 += ' '
Mensaje1 += 'mundo.'

#Ejecución
print(Mensaje1)

#La concatenación: Es una operación que consiste en unir dos cadenas o más, para formar una cadena de mayor tamaño.Operador(+).

#variables
mensaje2 = 'Hola'
espacio = ' '
nombre = 'Brayan'

#Ejecución
print(mensaje2 + espacio + nombre)

#Concatenación con Strings y Números

#Variables
val_uno = 1
val_dos = 2
resultado = val_uno + val_dos

#Conversion de Numeros a Cadenas
resultado = str(resultado)

#Ejecución
print('El resultado de la suma es: ' + resultado)
