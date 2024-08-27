Los **comentarios** en Python son líneas de texto dentro del código que son ignoradas por el intérprete al ejecutar el programa. Se utilizan para dejar notas, explicaciones, o descripciones sobre lo que hace el código, lo cual es útil para quienes leen o mantienen el código, incluido tú mismo en el futuro.

### Tipos de Comentarios en Python

1. **Comentarios de una sola línea**:
   - Se inician con el símbolo `#`. Todo lo que sigue después en esa línea es considerado un comentario y no se ejecuta.
   - Ejemplo:
     ```python
     # Este es un comentario de una sola línea
     print("Hola Mundo")  # Este comentario explica esta línea de código
     ```

2. **Comentarios de múltiples líneas**:
   - Aunque Python no tiene una sintaxis específica para comentarios de múltiples líneas, puedes usar múltiples líneas con `#` al inicio de cada línea.
   - También puedes utilizar comillas triples (`'''...'''` o `"""..."""`) para hacer lo que algunos llaman comentarios de bloque o comentarios de múltiples líneas. Sin embargo, estos en realidad crean una cadena de texto que no se asigna a ninguna variable, lo que algunos desarrolladores utilizan como comentario, aunque es más una convención que una característica oficial.
   - Ejemplo con múltiples `#`:
     ```python
     # Este es un comentario
     # de múltiples líneas
     # usando el símbolo de comentario en cada línea
     ```

   - Ejemplo con comillas triples:
     ```python
     """
     Este es un comentario de múltiples líneas
     usando comillas triples. Técnicamente es una cadena de texto,
     pero al no ser asignada a ninguna variable, es ignorada por el programa.
     """
     ```

### ¿Cuándo usar comentarios?

- **Explicar el propósito del código**: Útil cuando el código realiza operaciones complejas o no evidentes.
- **Anotar secciones del código**: Para marcar áreas importantes o dividir el código en secciones lógicas.
- **Recordatorios o "To-Dos"**: Para marcar áreas donde se necesita hacer algo en el futuro.
  ```python
  # TODO: Implementar la función de validación de datos
  ```

### Buenas prácticas con comentarios

- **Sé claro y conciso**: Los comentarios deben ser fáciles de entender.
- **Evita comentarios redundantes**: No comentes lo obvio; por ejemplo, no es necesario comentar `# Suma dos números` para una línea como `resultado = a + b`.
- **Mantén los comentarios actualizados**: Asegúrate de que los comentarios reflejen lo que hace el código actual.

Los comentarios son una herramienta poderosa para hacer que tu código sea más legible y mantenible, tanto para ti como para otros desarrolladores.