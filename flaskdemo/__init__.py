from flask import Flask
from .views.account import acct
from .views.account import inx





def create_app():
    app = Flask(__name__)
    app.config.from_object('settings.Config')
    app.register_blueprint(acct)
    app.register_blueprint(inx)



    return app