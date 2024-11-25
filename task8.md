# Constraint
* Añadir un constraint en cita para que la duración no pueda ser negativa
* Añadir restricción con _sql_constraints en el que el nombre de la cita sea único.

# Onchange
* Al cambiar el asignado de la cita, que el campo usuario se ponga con el usuario que lo ha modificado
* Cambiar la funcionalidad de partner_phone, quitar el related y añadir un onchange para que cuando se cambie el contacto se traiga el teléfono

# Actions
* Hacer un smartbutton para que en mascotas aparezcan las citas asociadas a esa mascota.
* Hacer smartbutton para que en mascotas, aparezcan los seguros asociados

# Default
* La cita cuando se cree, que tenga un usuario asignado.
* Cuando se cree la la cita que se ponga la fecha de hoy
* Cuando se cree un seguro que se ponga la fecha de ese dia

# Cron
* Cron que busque los seguros de manera diaria, si la fecha de expiración ha pasado, el campo expirado se pondrá a True
