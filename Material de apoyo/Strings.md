# ¿Qué son las cadenas de caracteres o Strings?

En Python, una **cadena de caracteres** (o *string*) es una secuencia de caracteres que se utiliza para representar texto. Las cadenas se pueden crear utilizando comillas simples (`'...'`), comillas dobles (`"..."`), comillas triples simples (`'''...'''`), o comillas triples dobles (`"""..."""`). Las comillas triples permiten definir cadenas de múltiples líneas.

### Ejemplos de Creación de Cadenas

```python
cadena1 = 'Hola'
cadena2 = "Mundo"
cadena_multilinea = """Esto es una cadena
que abarca varias líneas"""
```

### Operaciones Comunes con Cadenas

1. **Concatenación**: Se puede unir (concatenar) dos o más cadenas usando el operador `+`.

   ```python
   saludo = cadena1 + " " + cadena2
   print(saludo)  # Salida: Hola Mundo
   ```

2. **Repetición**: Las cadenas se pueden repetir usando el operador `*`.

   ```python
   risa = "ja" * 3
   print(risa)  # Salida: jajaja
   ```

3. **Acceso a Caracteres**: Se puede acceder a caracteres individuales de una cadena usando índices, donde el índice comienza en 0.

   ```python
   primera_letra = cadena1[0]
   print(primera_letra)  # Salida: H
   ```

4. **Rebanado (Slicing)**: Permite obtener una subsección de la cadena.

   ```python
   subcadena = cadena1[1:3]  # Obtiene caracteres desde el índice 1 hasta el 2
   print(subcadena)  # Salida: ol
   ```

5. **Longitud de una Cadena**: La función `len()` devuelve el número de caracteres en una cadena.

   ```python
   longitud = len(cadena1)
   print(longitud)  # Salida: 4
   ```

6. **Métodos Comunes de las Cadenas**:
   - `lower()` y `upper()` convierten la cadena a minúsculas o mayúsculas, respectivamente.
   - `strip()` elimina los espacios en blanco al inicio y al final de la cadena.
   - `replace(old, new)` reemplaza partes de la cadena.
   - `split(delimiter)` divide la cadena en una lista utilizando un delimitador.

   ```python
   texto = " Hola Mundo "
   print(texto.lower())      # Salida: hola mundo
   print(texto.strip())      # Salida: Hola Mundo
   print(texto.replace("Mundo", "Python"))  # Salida: Hola Python
   palabras = texto.split()  # Divide en palabras usando espacio como delimitador
   print(palabras)           # Salida: ['Hola', 'Mundo']
   ```

### Cadenas y Formateo

Python ofrece varias maneras de formatear cadenas:

1. **Formato Clásico**:

   ```python
   nombre = "Ana"
   edad = 30
   mensaje = "Me llamo %s y tengo %d años." % (nombre, edad)
   print(mensaje)  # Salida: Me llamo Ana y tengo 30 años.
   ```

2. **Método `format()`**:

   ```python
   mensaje = "Me llamo {} y tengo {} años.".format(nombre, edad)
   print(mensaje)  # Salida: Me llamo Ana y tengo 30 años.
   ```

3. **F-strings (Python 3.6 y posterior)**:

   ```python
   mensaje = f"Me llamo {nombre} y tengo {edad} años."
   print(mensaje)  # Salida: Me llamo Ana y tengo 30 años.
   ```

Las cadenas de caracteres en Python son extremadamente versátiles y ofrecen una amplia gama de operaciones para manipular texto.