from user import User, Friend
from flask import Flask, Blueprint
app = Flask(__name__)

def register(Targets):
    for Target in Targets:
        register_target=Blueprint(Target.__name__.lower(), __name__, template_folder='templates')
        register_target.add_url_rule('/', view_func=Target.as_view(Target.__name__.lower()))
        app.register_blueprint(register_target, url_prefix=f'/{Target.__name__.lower()}')
        print(Target.__name__)

register([User,Friend])
# register(Friend)
# users  = Blueprint('users', __name__, template_folder='templates')
# users.add_url_rule('/', view_func=UserView.as_view('user'))
# app.register_blueprint(users, url_prefix='/user')

