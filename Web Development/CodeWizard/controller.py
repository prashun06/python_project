import web
from CodeWizard.models.RegisterModel import RegisterModel
from CodeWizard.models.LoginModel import LoginModel
from CodeWizard.models.posts import Posts


web.config.debug = False

urls = (
    '/', 'Home',    # all are urls and urls map
    '/register', 'Register',
    '/login', 'Login',
    '/logout', 'Logout',
    '/post_registration', 'PostRegistration',
    '/check-login', 'CheckLogIn',
    '/post-activity', 'PostActivity'

)

app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore("session"), initializer={'user': None})
session_data = session._initializer


render = web.template.render('views/temlates', base='MainLayout', globals={'session': session_data, 'current_user': session_data["user"]})    # main landing page
#   class /routes


class Home:         # home page generation
    def GET(self):
        data = type('obj', (object,), {"username": "nick1", "password": "avocado1"})

        login = LoginModel.LoginModel()
        isCorrect = login.check_user(data)

        if isCorrect:
            session_data["user"] = isCorrect

        post_model = Posts.Posts()
        posts = post_model.get_all_posts()
        return render.home()


class Register:     # registration page generation
    def GET(self):
        return render.Register()


class Login:
    def GET(self):
        return render.login()


class PostRegistration:     # PostRegistration page generation
    def POST(self):
        data = web.input()
        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)
        return data.username


class CheckLogIn:
    def POST(self):
        data = web.input()
        login = Login.LoginModel()
        login.check_user(data)
        isCorrect = login.check_user(data)

        if isCorrect:
            session_data["user"] = isCorrect
            return isCorrect

        return "error"


class PostActivity:
    def POST(self):
        data = web.input()
        data.username = session_data['user']['username']

        post_model = posts.posts()
        post_model.insert_post(data)
        return "success"


class Logout:
    def GET(self):
        session['user'] = None
        session_data['user'] = None
        return "success"


if __name__ == "__main__":
    app.run()
