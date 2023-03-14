from flask import Blueprint, render_template
from flask.views import MethodView

# users  = Blueprint('users', __name__, template_folder='templates')

class User(MethodView): 
    def get(self):
        return render_template('index.html')
    def post(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass




class Friend(MethodView): 
    def get(self):
        return render_template('index2.html')
    def post(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass

# users.add_url_rule('/', view_func=UserView.as_view('user'))