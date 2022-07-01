import web

urls = (
    '/(.*)/(.*)', 'Index'  # "/" is connect to Index class and return it
                           #    (.*) is the elements 1st is name and 2 is age
)
render = web.template.render("resources/main.html")
app = web.application(urls, globals())    # app is to route to urls variable and pass to global or localhost


class Index:
    def GET(self, name, age):
        return render.main(name, age)    # return the object/arguments in display


if __name__ == "__main__":
    app.run()