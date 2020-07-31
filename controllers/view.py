import web

template = web.template.render("views/", base="template")

class ViewPerson:
    def GET(self):
        try:
            return template.view()
        except Exception as e:
            return "Error: "+str(e)
