import web
import database.conection as personas

model_personas = personas.Personas()

template = web.template.render("views/", base="template")

class ViewPerson:
    def GET(self, ID_PERSONA):
        try:
            result = model_personas.view(ID_PERSONA)[0]
            img = ""
            if result['SEXO']=='H':
                img = "../static/usuario.png"
            else:
                img = "../static/usuaria.png"
            return template.view(result, img)
        except Exception as e:
            return "Error "+str(e)