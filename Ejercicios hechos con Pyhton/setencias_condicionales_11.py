print ("Ejercicio de sentencias condicionales simples e ingreso de datos ")
#en este ejercicio estaresmo usando los conseptos aprendidos anteriormente
print("sistema para calcular el promedio de un alumno.")
nombre = input ("Señor alumno por favor ingrese su nombre:")
#generaremos las variables en las que estaremos guardando los datos de las calificaciónes 
matematicas = int (input (nombre +"¿Cuál es tu calificacíon en matemáticas?:"))
quimica = int (input (nombre + "¿Cuál es tu calificación en quimica?:"))
fisica = int (input (nombre + "¿Cuál es tu calificación en fisica?:"))
#generaremos una variable en donde alojaremos el promedio
promedio = (matematicas + quimica + fisica) / 3
#despues de haber pedido los valores de las materias haremos la operación para saber si se cumple la condición
if promedio >= 7:
    print ('Felicidades ' + nombre + '¡seras promovido a tu siguiente grado! con un promedio de :', int (promedio))
print ("fin.")
