import web
import database.conection as personas

model_persona = personas.Personas()

template = web.template.render("views/", base="template")

class Delete:
    def GET(self, ID_PERSONA):
            try:
                result = model_persona.view(ID_PERSONA)[0]
                img = ""
                if result['SEXO']=='H':
                    img = "../static/usuario.png"
                else:
                    img = "../static/usuaria.png"
                return template.delete(result, img)
            except Exception as e:
                return "Error: "+str(e)
    
    def POST(self, ID_PERSONA):
        try:
            form = web.input()
            id_persona = form.id_persona
            result = model_persona.delete(id_persona)
            web.seeother('/list')
        except Exception as e:
            print(e)
            return "Error"
