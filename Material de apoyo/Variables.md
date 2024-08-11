# ¿Qué son las variables en Python?

En Python, una **variable** es un nombre que se asocia con un valor almacenado en la memoria. Las variables se utilizan para guardar datos que pueden ser reutilizados y manipulados a lo largo de un programa. A diferencia de algunos otros lenguajes de programación, en Python no es necesario declarar explícitamente el tipo de la variable; el tipo se infiere automáticamente en función del valor asignado.

---

### Creación y Asignación de Variables

Para crear una variable en Python, simplemente se elige un nombre y se asigna un valor usando el operador `=`. Por ejemplo:

```python
x = 10
nombre = "Juan"
pi = 3.14159
```

En este ejemplo:
- `x` es una variable que almacena el valor entero `10`.
- `nombre` es una variable que almacena la cadena de texto `"Juan"`.
- `pi` es una variable que almacena el número en punto flotante `3.14159`.

---

### Reglas para Nombrar Variables

- Los nombres de variables deben comenzar con una letra (a-z, A-Z) o un guion bajo (`_`), seguido de letras, números o guiones bajos.
- No pueden comenzar con un número.
- Son sensibles a mayúsculas y minúsculas, lo que significa que `variable`, `Variable`, y `VARIABLE` son tres variables diferentes.
- No deben usar palabras reservadas de Python como nombres de variables (como `for`, `while`, `if`, `else`, etc.).

---

### Ejemplo de Uso

```python
# Asignación de valores a variables
a = 5
b = 7
suma = a + b

# Imprimir el resultado
print("La suma de", a, "y", b, "es", suma)
```

En este caso, la variable `suma` almacena el resultado de sumar las variables `a` y `b`. Luego, el resultado se imprime en la consola.