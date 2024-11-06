from account import Account
import transaction

def create_account(root, account_id):
    """
    Crea una nueva cuenta y la guarda en la base de datos.
    """
    if account_id in root.accounts:
        print(f"La cuenta '{account_id}' ya existe.")
        return

    root.accounts[account_id] = Account()
    transaction.commit()
    print(f"Cuenta '{account_id}' creada y guardada en la base de datos.")


def read_account(root, account_id):
    """
    Lee una cuenta específica por su ID.
    """
    if account_id in root.accounts:
        account = root.accounts[account_id]
        print(f"Cuenta '{account_id}' encontrada: Balance = {account.balance}")
        return account
    else:
        print(f"La cuenta '{account_id}' no existe.")
        return None


def update_account(root, account_id, amount, action):
    """
    Actualiza el balance de una cuenta realizando una operación de depósito o retiro.
    """
    if account_id in root.accounts:
        account = root.accounts[account_id]
        if action == 'deposito':
            account.deposit(amount)
            transaction.commit()
            print(f"Se ha depositado {amount} en la cuenta '{account_id}'. Nuevo balance: {account.balance}")
        elif action == 'retiro':
            try:
                account.cash(amount)
                transaction.commit()
                print(f"Se ha retirado {amount} de la cuenta '{account_id}'. Nuevo balance: {account.balance}")
            except AssertionError:
                print(f"No se puede retirar {amount}. Fondos insuficientes en la cuenta '{account_id}'.")
                rollback_changes()
    else:
        print(f"La cuenta '{account_id}' no existe.")


def delete_account(root, account_id):
    """
    Elimina una cuenta específica de la base de datos.
    """
    if account_id in root.accounts:
        del root.accounts[account_id]
        transaction.commit()
        print(f"La cuenta '{account_id}' ha sido eliminada de la base de datos.")
    else:
        print(f"La cuenta '{account_id}' no existe.")


def rollback_changes():
    """
    Revierte cualquier cambio no confirmado.
    """
    transaction.abort()
    print("Cambios no confirmados han sido revertidos.")


def list_accounts(root):
    """
    Muestra todas las cuentas almacenadas en la base de datos.
    """
    print("Cuentas almacenadas:")
    if not root.accounts:
        print("No hay cuentas registradas en la base de datos.")
        return

    for account_id, account in root.accounts.items():
        print(f"ID de cuenta: {account_id} - Balance: {account.balance}")
