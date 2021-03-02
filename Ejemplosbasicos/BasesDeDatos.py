import mysql.connector

class ConexionBD:

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="cursopython",
            database="personal"
        )
        self.cur = self.mydb.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # close db connection
        self.mydb.close()