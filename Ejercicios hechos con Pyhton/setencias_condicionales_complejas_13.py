print ("Estaremos calculando el promedio de un alumno")
#usaremos las sentencias condiconales complejas y la entrada de datos.
print ("Bienvenido, por favro ingrese un nombre ")
nombre = input ("¿Cual es tu nombre?:")
print  (nombre + " bienvenido,ingrese sus clificaciones")
# Variables en las cuales se guardan los datos de las materias,estos datos son de números flotatantes o reales.
# Se solicitan números de tipo flotantes para ser mas exactos.  
mate = float  (input (nombre + "¿Cuál es tu Calificación de matematicas?:"))
quimi = float (input (nombre + "¿Cuál es tu Calificación de quimica?:"))
esp = float  (input (nombre + "¿Cuál es tu calificación de Calificación de español:"))
# Variable en la cual se realizará la operación.
promedio = (mate + quimi + esp)/3
# Sentencia condicional compleja.
#para redondear el promedio usamos el comando de round que nos permite mostrar las decimas que queramos mostar.
if promedio >= 7:
    print ("Felicidades " ,nombre ," seras promovido al siguiente año,su promedio fue de :",round (promedio,2))
else:
    print (nombre ,"desafortunadamente tendrás que repetir el año,su promedio fue de :", round (promedio,2))
print ("gracias por usar el sistema que tenga una feliz tarde")
