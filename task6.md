# Opciones m2o

En Citas no se debe de poder acceder al contacto ni crear contactos nuevos de manera rápida, pero si desde vista de formulario.
En Mascotas no se debe de poder crear una especie nueva, solo elegir.

# Modelo nuevo acciones a realizar en una cirugía

Vamos a crear por una parte un modelo nuevo llamado acciones a realizar. Este modelo va a ser un one2many para las cirugías.

Va a tener un campo de secuencia, nombre y un campo estado (Borrador y hecho) // Igual que en cirugía

# Vista embembida

Vamos a añadir este modelo como vista embebida en cirugía

# Contexto

Vamos a decir desde contexto, que el campo por defecto del estado de la acción sea el estado de la cirugía

