import web

urls = (
    '/', 'Index',
    '/list', 'controllers.list.List',
    '/insert', 'controllers.insert.Insert',
    '/delete', 'controllers.delete.Delete',
    '/update', 'controllers.update.Update',
    '/view', 'controllers.view.ViewPerson'
)
app = web.application(urls, globals())

render = web.template.render("views/", base="template")

class Index:
    def GET(self):
        return render.index()

if __name__ == "__main__":
    app.run()