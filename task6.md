# Vistas relacionadas

Crear dos vistas simples para alergias, vista de arbol y formulario.
Pasar esas vistas por contexto en la mascota.
Darle prioridad 100 para que no rompa las vistas normales de alergias.

# Opciones m2o

En Citas no se debe de poder acceder al usuario ni crear usuarios nuevos de manera rápida, pero si desde vista de formulario.
En Mascotas no se debe de poder crear una especie nueva, solo elegir.

# Modelo nuevo acciones a realizar en una cirugía

Vamos a crear por una parte un modelo nuevo llamado acciones a realizar. Este modelo va a ser un one2many para las cirugías.

Va a tener un campo nombre de secuencia, nombre y un campo estado (Borrador y hecho) // Igual que en cirugía

# Vista embembida

Vamos a añadir este modelo como vista embebida en cirugía

# Contexto

Vamos a decir desde contexto, que el campo por defecto del estado de la acción sea el estado de la incidencia

