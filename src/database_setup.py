import ZODB, ZODB.FileStorage
import BTrees.OOBTree


def initialize_database():
    """
    Configura la base de datos de ZODB y devuelve la instancia de la base de datos.
    """
    # Almacena la base de datos en un archivo local
    almacenamiento = ZODB.FileStorage.FileStorage('archivo.fs')

    # Instancia la base de datos y la conecta con el almacenamiento
    bd = ZODB.DB(almacenamiento)

    return bd


def open_connection(bd):
    """
    Abre una conexión a la base de datos y devuelve la conexión y el objeto raíz.
    """
    # Conexión a la base de datos
    conexion = bd.open()

    # Acceso a la raíz del árbol de datos
    root = conexion.root

    # Si no existe el árbol de cuentas, se crea
    if not hasattr(root, 'accounts'):
        root.accounts = BTrees.OOBTree.BTree()

    return conexion, root
