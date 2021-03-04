import BasesDeDatos

#with BasesDeDatos.ConexionBD("localhost", "root", "cursopython", "personal") as base:
#with BasesDeDatos.ConexionBD("sql10.freemysqlhosting.net", "sql10396651", "rQWRh3vJtk", "sql10396651") as base:
with BasesDeDatos.ConexionBD("db4free.net", "rootzabala", "cursopython", "personalzabala") as base:
    #base.cur.execute("SHOW TABLES")
    base.cur.execute("Select * from alumnos")
    for tab in base.cur:
        print(tab)

