# ¿Qué son las palabras reservadas en Python?

Las **palabras reservadas** en Python son identificadores especiales que tienen un significado específico para el lenguaje y no pueden ser utilizados como nombres de variables, funciones, clases, u otros identificadores definidos por el usuario. Estas palabras forman parte de la sintaxis de Python y están reservadas porque controlan la estructura del código.

### Lista de Palabras Reservadas en Python

A continuación, se muestra una lista de las palabras reservadas en Python (versión 3.8 y posteriores):

- `False`
- `await`
- `else`
- `import`
- `pass`
- `None`
- `break`
- `except`
- `in`
- `raise`
- `True`
- `class`
- `finally`
- `is`
- `return`
- `and`
- `continue`
- `for`
- `lambda`
- `try`
- `as`
- `def`
- `from`
- `nonlocal`
- `while`
- `assert`
- `del`
- `global`
- `not`
- `with`
- `async`
- `elif`
- `if`
- `or`
- `yield`

### Uso de las Palabras Reservadas

Estas palabras se utilizan para controlar la lógica y estructura del programa. Aquí algunos ejemplos:

- **Control de flujo**:
  - `if`, `elif`, `else`: Se utilizan para realizar evaluaciones condicionales.
    ```python
    if True:
        print("Es verdadero")
    elif False:
        print("Es falso")
    else:
        print("Ninguno")
    ```

  - `for`, `while`: Se utilizan para crear bucles.
    ```python
    for i in range(5):
        print(i)

    while True:
        break
    ```

- **Manejo de excepciones**:
  - `try`, `except`, `finally`, `raise`: Para manejar errores y excepciones.
    ```python
    try:
        x = 1 / 0
    except ZeroDivisionError:
        print("División por cero no permitida")
    finally:
        print("Fin del bloque try-except")
    ```

- **Definición de funciones y clases**:
  - `def`, `class`: Para definir funciones y clases, respectivamente.
    ```python
    def mi_funcion():
        return "Hola"

    class MiClase:
        pass
    ```

- **Manejo de valores booleanos y operadores lógicos**:
  - `True`, `False`, `and`, `or`, `not`: Para trabajar con lógica booleana.
    ```python
    es_mayor = True
    es_menor = False

    if es_mayor and not es_menor:
        print("Lógica booleana funciona")
    ```

### Importante:

- Python distingue entre mayúsculas y minúsculas, por lo que `True` y `true` se tratan de manera diferente; la primera es una palabra reservada, y la segunda puede ser un nombre de variable.
- No se deben usar estas palabras como nombres de variables u otros identificadores, ya que hacerlo generará un error de sintaxis.

Si deseas ver la lista completa de palabras reservadas en tu entorno de Python, puedes usar el siguiente código:

```python
import keyword
print(keyword.kwlist)
```

Este código imprimirá todas las palabras reservadas en la versión de Python que estés utilizando.