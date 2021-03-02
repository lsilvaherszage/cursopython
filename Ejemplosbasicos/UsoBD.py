import BasesDeDatos

with BasesDeDatos.ConexionBD() as base:
    base.cur.execute("SHOW TABLES")
    
    for tab in base.cur:
        print(tab)

