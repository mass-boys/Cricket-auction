from flask import Flask 

def create_app():
    app = Flask(__name__)    

    from .views import main as main_blueprint
    from .test import test as test_blueprint


    app.register_blueprint(main_blueprint)
    app.register_blueprint(test_blueprint,url_prefix = "/test")

    return app
