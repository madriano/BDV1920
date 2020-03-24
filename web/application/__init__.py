"""Initialize the application"""

from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()

def create_app(test_config=None):
    """Construct the core application"""
    app = Flask(__name__, instance_relative_config=False)

    # Application Configuration
    app.config.from_object('config.Config')

    #db.init_app(app)

    with app.app_context():
    
         # Create database tables for our models
        #db.create_all()
        from . import routes

        # routes will be attached from now on

        return app
