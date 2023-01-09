print ("======================")
print ("sistema de comparación")
print ("======================\n")
#haremos un sistema de comparación númerica.
print ("Introduzca dos números a comparar:\n")
num_uno = int (input ("Introduzca el primer digito:"))
num_dos = int (input ("Introduzca el segundo digito:"))
# Se realiza la comparación
print ("\nlos números a comparar son ",num_uno, " y ",num_dos, "\n")
# sentencia condicional
if num_uno == num_dos:
    print ("Es igual.")
if num_uno != num_dos:
    print ("Es diferente.")
if num_uno < num_dos:
    print ("Es menor.")
if num_uno > num_dos:
    print ("Es mayor.")
if num_uno <= num_dos:
    print ("Es menor igual.")
if num_uno >= num_dos :
    print ("Es mayor igual.")
#Fin de la sentencia condicional
print ("fin,gracias por usar nuestro programa")
