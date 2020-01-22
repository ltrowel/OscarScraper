import mysql.connector


class OscarDAO:

    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="oscars_user",
            passwd="password123",
            database="oscars",
            auth_plugin='mysql_native_password'
        )

    def get_awards(self):
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT id, name, has_nominee FROM tblaward"
        )

        return cursor.fetchall()
