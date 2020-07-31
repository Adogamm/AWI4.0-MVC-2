import web
import database.conection as personas

model_personas = personas.Personas()

template = web.template.render("views/", base="template")

class Update:
    def GET(self, ID_PERSONA):
        try:
            model_personas.connect()
            result = model_personas.view(ID_PERSONA)[0]
            img = ""
            sex = ""
            estado_origen = result['ESTADO']
            if result['SEXO']=='H':
                img = "../static/usuario.png"
                sex = "Hombre"
            else:
                img = "../static/usuaria.png"
                sex = "Mujer"
            
            return template.update(result, img, sex, estado_origen)
        except Exception as e:
            return "Error: "+str(e)

    def POST(self, ID_PERSONA):
        try:
            form = web.input()
            id_persona = form.id_persona
            matricula = form.matricula
            nombre = form.nombre
            primer_apellido = form.primer_apellido
            segundo_apellido = form.segundo_apellido
            edad = form.edad

            if form.sexo == "1":
                sexo = "H"
            elif form.sexo == "2":
                sexo = "M"

            if form.estado == "1":
                estado = "Aguascalientes"
            elif form.estado == "2":
                estado = "Baja California Norte"
            elif form.estado == "3":
                estado = "Baja California Sur"
            elif form.estado == "4":
                estado = "Campeche"
            elif form.estado == "5":
                estado = "Coahuila"
            elif form.estado == "6":
                estado = "Colima"
            elif form.estado == "7":
                estado = "Chiapas"
            elif form.estado == "8":
                estado = "Chihuahua"
            elif form.estado == "9":
                estado = "Ciudad de México"
            elif form.estado == "10":
                estado = "Durango"
            elif form.estado == "11":
                estado = "Guanajuato"
            elif form.estado == "12":
                estado = "Guerrero"
            elif form.estado == "13":
                estado = "Hidalgo"
            elif form.estado == "14":
                estado = "Jalisco"
            elif form.estado == "15":
                estado = "México"
            elif form.estado == "16":
                estado = "Michoacán"
            elif form.estado == "17":
                estado = "Morelos"
            elif form.estado == "18":
                estado = "Nayarit"
            elif form.estado == "19":
                estado = "Nuevo León"
            elif form.estado == "20":
                estado = "Oaxaca"
            elif form.estado == "21":
                estado = "Pueba"
            elif form.estado == "22":
                estado = "Querétaro"
            elif form.estado == "23":
                estado = "Quintana Roo"
            elif form.estado == "24":
                estado = "San Luis Potosí"
            elif form.estado == "25":
                estado = "Sinaloa"
            elif form.estado == "26":
                estado = "Sonora"
            elif form.estado == "27":
                estado = "Tabasco"
            elif form.estado == "28":
                estado = "Tamaulipas"
            elif form.estado == "29":
                estado = "Tlaxcala"
            elif form.estado == "30":
                estado = "Veracruz"
            elif form.estado == "31":
                estado = "Yuxatán"
            elif form.estado == "32":
                estado = "Zacatecas"
            result = model_personas.update(id_persona, matricula, nombre, primer_apellido, segundo_apellido, edad, sexo, estado)
            web.seeother('/list')
        except Exception as e:
            print("Error: "+str(e))
            return False
