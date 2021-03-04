import mysql.connector

class ConexionBD:

    def __init__(self, host, user, passwd, database):
        self.host=host
        self.user=user
        self.passwd=passwd
        self.database=database
        self.mydb = mysql.connector.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd,
            database=self.database
        )
        self.cur = self.mydb.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # close db connection
        self.mydb.close()