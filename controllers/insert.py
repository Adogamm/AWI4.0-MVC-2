import web

template = web.template.render("views/", base="template")

class Insert:

    def GET(self):
        try:
            return template.insert()
        except Exception as e:
            return "Error: "+str(e)
    
    def POST(self):
        try:
            form = web.input()
            print(form.nombre)
            print(form.matricula)
            if form.estado == "1":
                print("Aguascalientes")
            if form.sexo == "1":
                print("Hombre")
            elif form.sexo == "2":
                print("Mujer")
        except Exception as e:
            return "Error"+str(e)
