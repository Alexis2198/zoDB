from database_setup import initialize_database, open_connection
from account_operations import create_account, read_account, update_account, delete_account, list_accounts, rollback_changes

# Configura la base de datos
bd = initialize_database()
conexion, root = open_connection(bd)

# Crear cuentas
create_account(root, 'cuenta-1')
create_account(root, 'cuenta-2')

# Listar cuentas
list_accounts(root)

# Leer una cuenta específica
read_account(root, 'cuenta-1')

# # Actualizar una cuenta (ejemplo de depósito y retiro)
update_account(root, 'cuenta-1', 100, 'deposito')
update_account(root, 'cuenta-1', 50, 'retiro')

# # Eliminar una cuenta
delete_account(root, 'cuenta-2')

# # Listar cuentas nuevamente para verificar cambios
list_accounts(root)

# # Ejemplo de rollback
rollback_changes()

# Cierra la conexión y base de datos
conexion.close()
bd.close()
