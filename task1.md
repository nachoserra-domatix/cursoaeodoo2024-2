# Añadir seguridad (7)

Hacer dos grupos de usuario, manager y user.
El usuario solo podrá ver y modificar las citas que tenga asignadas (crearemos un campo user_id)
El manager podrá crear, borrar ver y modificar cualquier cita

# Vistas (9)
Añadir campos secuencia(integer), solución(html) y responsable(many2one)

## Vista tipo lista:
Añadir campo sequence con widget handle
Mostrar nombre, fecha,responsable, y estado
Campo fecha que sea opcional y mostrarlo por defecto
Campo responsable que sea opcional pero ocultarlo

## Vista formulario
Header con el estado, nombre h1 como en pedidos y dos columnas:
Fecha/Responsable y duración


## Solapas:
razón y solución

# Modelo veterinary.pet
* Crear vistas de lista y de formulario
* Añadir al ir.model.access.csv los grupos de user y manager
