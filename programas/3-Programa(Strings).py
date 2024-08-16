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


#Busqueda: Consiste en localizar dentro de una cadena, una subcadena más pequeña a un caracter. Para lo cual es necesario utilizar el método FIND
# Variables
mensaje3 = 'Hola Mundo!'
buscar_subcadena = mensaje3.find('Mundo!')
conversion = str(buscar_subcadena)

#Ejecución 
print('Este es el resultado de la busqueda:' + conversion)

#Extracción: Se trata de sacar fuera de una cadena, una porción de la misma según su posición dentro de ella. Para ello es necesario indicar la posición a extraer [1:5]
#Variables 
mensaje4 = 'Hola mundo!'
extraer_cadena = mensaje4[5:10]

#Ejecución 
print('Este es el resultado de la extración: ' + extraer_cadena)

#Comparación: Se utiliza para comparar dos cadenas de caracteres. para ello se utiliza el operador (==)
comparacion_1 = 'Hola mundo!'
comparacion_2 = 'Hola mundo!'
operacion = comparacion_1 == comparacion_2
conversion_ = str(operacion)

#Ejecución 
print('El resultado de la comparción es: ' + conversion_)

