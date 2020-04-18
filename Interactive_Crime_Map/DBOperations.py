import pymysql
import dbConfig

class DBHelper:

    def connect(self, database = 'crimemap'):
        return pymysql.connect(host = dbConfig.db_host,
                                port = dbConfig.db_port,
                                user = dbConfig.db_user,
                                password = dbConfig.db_password,
                                db = database)
    
    def get_all_inputs(self):
        connection = self.connect()
        try:
            query = "select description from crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
            return cursor.fetchall()
        finally:
            connection.close()
    
    def add_input(self, data):
        connection = self.connect()
        try:
            query = "insert into crimes(description) values ('{}');".format(data)
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()
    
    def clean_all(self):
        connection = self.connect()
        try:
            query = "delete from crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()