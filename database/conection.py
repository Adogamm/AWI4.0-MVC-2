import mysql.connector

class Personas():
    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                user = 'AdolfoLeBa',
                password = 'SoyAdolfo_1',
                host = '127.0.0.1',
                database = 'REGISTRO',
                auth_plugin='mysql_native_password'
            )
            self.cursor = self .cnx.cursor(buffered=True)
        except Exception as e:
            print(e)

    def select(self):
        try:
            self.connect()
            query = ("SELECT * FROM PERSONAS;")
            self.cursor.execute(query)
            result = []
            for row in self.cursor:
                diccionario ={
                    "ID_PERSONA":row[0],
                    "MATRICULA":row[1],
                    "NOMBRE":row[2],
                    "PRIMER_APELLIDO":row[3],
                    "SEGUNDO_APELLIDO":row[4],
                    "EDAD":row[5],
                    "SEXO":row[6],
                    "ESTADO":row[7],
                }
                result.append(diccionario)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)
            result = []
            return result

objeto = Personas()
objeto.connect()
for row in objeto.select():
    print(row)