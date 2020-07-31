import web

template = web.template.render("views/", base="template")

class Update:
    def GET(self):
        try:
            return template.update()
        except Exception as e:
            return "Error: "+str(e)
