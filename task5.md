# Campos calculados

* Crear campo Asignado en Citas, el cual comprobará: Si hay responsable, asignado pasa a ser True y si no lo hay estará a False
* Calcular la edad de la mascota a partir del campo fecha de nacimiento

# Campos relacionales

* Añadir campo de contacto (partner_id)
* Añadir un campo en Citas que muestre el teléfono del contacto

# Campo calculado guardado en base de datos

* Crear un campo calculado que que diga los días restantes para que el seguro expire

# ORM

* En una mascota, botón que permita crear un seguro para esa mascota.

* En una cita, botón que genere etiquetas en base a los motivos y a la especie de la mascota. Que los busque si ya existen esas etiquetas, después se asignan y si no las crea y las asigna.

# Deberes
* El campo vacunado se rellenará a True si se añade una fecha de última vacunación y si se activa, se rellenará la fecha con el día en el que se active
* Campo relacional en citas que aparezca el correo electrónico del contacto
* En el modelo de alergia, crear un campo entero de prioridad, guardado en base de datos, que asigne estrellas dependiendo de la severidad
* Desde una mascota, marcar todas las cirugías de esa mascota como completada
