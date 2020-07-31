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

    def view(self, ID_PERSONA):
        try:
            self.connect()
            query = ("SELECT * FROM PERSONAS WHERE ID_PERSONA = %s;")
            values = (ID_PERSONA,)
            self.cursor.execute(query, values)
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

    def insert(self, matricula, nombre, primer_apellido, segundo_apellido, edad, sexo, estado):
        try:
            self.connect()
            query = ("INSERT INTO PERSONAS (MATRICULA, NOMBRE, PRIMER_APELLIDO, SEGUNDO_APELLIDO, EDAD, SEXO, ESTADO) VALUES (%s, %s, %s, %s, %s, %s, %s);")
            values = (matricula, nombre, primer_apellido, segundo_apellido, edad, sexo, estado)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False

objeto = Personas()
objeto.connect()
for row in objeto.view(1):
    print(row)