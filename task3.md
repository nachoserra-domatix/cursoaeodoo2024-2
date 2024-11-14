
# Modelos nuevos

* Modelo de especies (reemplazamos el campo species por un objeto)
  * Nombre   

* Modelo de cirugías (veterinary.surgery)
  * Nombre
  * Mascota (veterinary.pet)
  * Empleado (hr.employee) (añadir en dependncias el módulo hr)
  * Fecha de la cirugía
  * Estado
    
* Modelo de alergias (veterinary.allergy)
  * Nombre
  * Grado de severidad
  * Descripción
   
    
* Modelo de seguro médico (veterinary.insurance)
  * Mascota
  * Compañía de seguros
  * Número de póliza
  * Detalles de cobertura
  * Fecha de expiración
  * Expirado
 
# Seguridad

Añadir la seguridad para todos los modelos nuevos que hemos creado. El manager tiene que poder hacerlo todo, el usuario a vuestro gusto, pero mínimo un tipo de operación a 0

# Vistas

Crear menú, acción y vista de árbol y formulario para cada modelo nuevo.

# Métodos

Añadir método o métodos que hagan un flujo de estados en el modelo de cirugía. Por ejemplo, Pasar a hecha, o en progreso.
Añadir método en seguro médico que verifique si la fecha ha expirado. Si lo ha hecho, marcar el campo de Expirado a True


# Traducir

Traducir todo.

