# Crear modulo nuevo

# Herencia por extensión
* En el modulo nuevo heredar el modelo de citas y añadir un many2one de pedido de venta
* Heredar citas y añadir botón de crear pedido de venta
* Heredar sale.order y añadirle la cita asociada en otra información.

# Heredar método
* Heredar método de crear y añadir una secuencia a las citas

# Herencia por delegación
* Crear modelo de veterinario
* En el modelo de veterinario que tenemos añadirle herencia por delegación con inherits y probar después a añadir a la vista campos de res.partner como por ejemplo street,city y country_id

# Deberes
* Heredar el botón de cancelar cita, para que si se cancela y hay pedidos con esa cita, se cancelen y eliminen
* Añadir botón en citas que confirme la venta y facture el pedido asociado

