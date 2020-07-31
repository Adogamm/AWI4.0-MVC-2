import web

template = web.template.render("views/", base="template")

class Delete:
    def GET(self):
            try:
                return template.delete()
            except Exception as e:
                return "Error: "+str(e)
