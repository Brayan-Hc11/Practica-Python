# Operadores Aritméticos

Los **operadores aritméticos** en Python se utilizan para realizar operaciones matemáticas básicas sobre números. A continuación, se describen los operadores aritméticos más comunes:

### Operadores Aritméticos Básicos

1. **Suma (`+`)**:
   - Se utiliza para sumar dos números.
   - Ejemplo:
     ```python
     resultado = 5 + 3
     print(resultado)  # Salida: 8
     ```

2. **Resta (`-`)**:
   - Se utiliza para restar un número de otro.
   - Ejemplo:
     ```python
     resultado = 10 - 4
     print(resultado)  # Salida: 6
     ```

3. **Multiplicación (`*`)**:
   - Se utiliza para multiplicar dos números.
   - Ejemplo:
     ```python
     resultado = 7 * 6
     print(resultado)  # Salida: 42
     ```

4. **División (`/`)**:
   - Se utiliza para dividir un número entre otro. El resultado es un número de punto flotante (decimal).
   - Ejemplo:
     ```python
     resultado = 15 / 3
     print(resultado)  # Salida: 5.0
     ```

5. **División Entera (`//`)**:
   - Se utiliza para dividir un número entre otro, pero solo devuelve la parte entera del cociente (sin los decimales).
   - Ejemplo:
     ```python
     resultado = 17 // 3
     print(resultado)  # Salida: 5
     ```

6. **Módulo (`%`)**:
   - Devuelve el resto de la división entre dos números.
   - Ejemplo:
     ```python
     resultado = 17 % 3
     print(resultado)  # Salida: 2
     ```

7. **Potenciación (`**`)**:
   - Eleva un número a la potencia de otro número.
   - Ejemplo:
     ```python
     resultado = 2 ** 3
     print(resultado)  # Salida: 8
     ```

### Ejemplos de Uso en Python

```python
# Suma
suma = 8 + 2
print("Suma:", suma)  # Salida: Suma: 10

# Resta
resta = 8 - 2
print("Resta:", resta)  # Salida: Resta: 6

# Multiplicación
multiplicacion = 8 * 2
print("Multiplicación:", multiplicacion)  # Salida: Multiplicación: 16

# División
division = 8 / 2
print("División:", division)  # Salida: División: 4.0

# División Entera
division_entera = 8 // 3
print("División Entera:", division_entera)  # Salida: División Entera: 2

# Módulo
modulo = 8 % 3
print("Módulo:", modulo)  # Salida: Módulo: 2

# Potenciación
potencia = 2 ** 3
print("Potencia:", potencia)  # Salida: Potencia: 8
```

### Precedencia de Operadores

Al igual que en las matemáticas, los operadores aritméticos tienen una precedencia que determina el orden en el que se realizan las operaciones:

1. **Potenciación (`**`)** tiene la mayor precedencia.
2. **Multiplicación (`*`), División (`/`), División Entera (`//`), y Módulo (`%`)** tienen la misma precedencia y se evalúan de izquierda a derecha.
3. **Suma (`+`) y Resta (`-`)** tienen la menor precedencia y también se evalúan de izquierda a derecha.

Puedes usar paréntesis `()` para cambiar el orden de evaluación si es necesario.

```python
resultado = 2 + 3 * 4  # Se evalúa como 2 + (3 * 4)
print(resultado)  # Salida: 14

resultado_con_parentesis = (2 + 3) * 4
print(resultado_con_parentesis)  # Salida: 20
```

Los operadores aritméticos son fundamentales para realizar cálculos en Python y son ampliamente utilizados en casi todos los programas.