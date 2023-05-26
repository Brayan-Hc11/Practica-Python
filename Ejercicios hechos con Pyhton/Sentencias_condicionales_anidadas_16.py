print ("=====================")
print ("Sistema de convervión")
print ("===================== \n")
# Bienvenido
print ("Bienvenido a nuestro sistema de converición númerica \n")
# Establecemos el menú
print ("Menú de opciones: \n")
print ("Precione 1 para convertir de números a palabras.")
print ("Precione 2 para convertir de palabras a números. \n")
# Establcemos la primera sentencia condicional
opcion = int (input ("¿Cual es la opción que desea?:"))
if opcion == 1:
    print ("\n A escojido el Covertidor de número a palabra \n")
# Anidamos la primera sentencia condicional multiple    
    op_uno = int (input ("¿Cúal es el número que desea convertir a letras?: "))
    if op_uno == 1:
        print ("El resultado es: uno \n")
    elif op_uno == 2:
        print ("El resultado es: dos \n")
    elif op_uno == 3:
        print ("El resultado es: tres \n")
    elif op_uno == 4:
        print ("El resultado es: cuatro \n")
    elif op_uno == 5:
        print ("El resultado es: cinco \n")
    else:
        print ("Este convertidor esta disponible hasta el número cinco. \n")
       
elif opcion == 2:
    print ("\n A escojido el  Convertidor de palabra a número \n")
# Anidamos la segunda sentencia condicional multiple
    op_dos = input("¿Cúal es la palabra que desea convertir a número?: ")
# El comando de .lower() nos permite convertir una cadena de caracteres mayusculas a minusculas.
    op_dos = op_dos.lower()
    if op_dos == "uno":
        print ("El resultado es: 1 \n")
    elif op_dos == "dos":
        print ("El resultado es: 2 \n")
    elif op_dos == "tres":
        print ("El resultado es: 3 \n")
    elif op_dos == "cuatro":
        print ("El resultado es: 4 \n")
    elif op_dos == "cinco":
        print ("El resultado es: 5 \n")
    else:
        print ("Este convertidor solo esta disponible hasta el número 5. \n")
else :
    print ("Esta opción no esta disponible \n")
print ("Fin del proceso")


