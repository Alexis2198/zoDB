import ZODB, ZODB.FileStorage
#Almacena la base de datos en un archivo local
almacenamiento = ZODB.FileStorage.FileStorage('archivo.fs')
#Instanciación de la base de datos y conexión con el almacenamiento
bd = ZODB.DB(almacenamiento)

conexion = bd.open()
root = conexion.root

from account import Account
import BTrees.OOBTree

root.accounts = BTrees.OOBTree.BTree()
root.accounts['account-1'] = Account()

import transaction

transaction.commit()
transaction.abort()
