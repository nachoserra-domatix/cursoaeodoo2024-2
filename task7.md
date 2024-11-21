
## Modelo nuevo de Adopción
* Nombre
* Fecha de entrada al refugio
* Fecha de adopción
* Mascota
* Contacto de la persona que adoptará
* Estado de la adopción (many2one)
* Usuario responsable
* Dias en refugio
* Notas
* Tarifa de adopción

## Modelo nuevo de estado de la adopción
* Nombre
* Adoptado(boolean)

## Modificaciones modelo de mascota
* Añadir campo de imagen para la foto de mascota
* Añadir el campo de alergias como many2many
* Añadir boolean de adoptado

## Modificaciones modelo lineas de cita
* Añadir campo subtotal
* 
## Modificaciones modelo de cita
* Añadir campo de total

## Vistas de adopciones
* Vista árbol, formulario, pivot y kanban.
* La vista kanban a vuestro gusto pero intentad añadir la foto de la mascota cuando esté enlazada a una y agrupado por las etapas de adopción

## Vista de mascota
* Añadir las alergias de manera embebida en la vista formulario
* Añadir la foto en vista formulario
* Añadir el check de adoptado

## Filtros en adopciones
* Filtro para poder buscar por nombre, usuario, y contacto.
* Haced que el primer filtro de nombre también busque además por mascota y notas
* Filtro para saber que adopciones han finalizado (es decir han adoptado a la mascota)
* Filtro para saber que adopciones todavía no han finalizado.
* Permitir agrupar usuario responsable.

## Vistas de citas y lineas:
* Añadir subtotal y total en los modelos

## Dominio
En las adopciones, al desplegar el many2one de mascota pueden aparecer mascotas ya adoptadas


# Campos calculados
* Calcular en el modelo de adopciones los días que ha pasado una mascota en el refugio.
* Calcular el subtotal del modelo lineas de cita basandonos en la cantidad y el precio unitario.
* Calcular el total en el modelo cita basándonos en el subtotal de las lineas.
