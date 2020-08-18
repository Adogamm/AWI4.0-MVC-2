import mysql.connector

class Personas():
    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                user = 'ykrqakjreho5ixu4',
                password = 't4e32ci83m3amuuq',
                host = 'z37udk8g6jiaqcbx.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
                port = 3306,
                database = 'hd3tg32ltrpxg4m2',
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
    
    def update(self, id_persona, matricula, nombre, primer_apellido, segundo_apellido, edad, sexo, estado):
        try:
            self.connect()
            query = ("UPDATE PERSONAS SET MATRICULA=%s, NOMBRE=%s, PRIMER_APELLIDO=%s, SEGUNDO_APELLIDO=%s, EDAD=%s, SEXO=%s, ESTADO=%s WHERE ID_PERSONA=%s;")
            values = (matricula, nombre, primer_apellido, segundo_apellido, edad, sexo, estado, id_persona)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self, id_persona):
        try:
            self.connect()
            query = ("DELETE FROM PERSONAS WHERE ID_PERSONA=%s;")
            values = (id_persona,)
            self.cursor.execute(query,values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False
