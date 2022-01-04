# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
#
# db = SQLAlchemy()
#
#
# def init_app():
#     app = Flask(__name__)
#     app.config['DEBUG'] = True
#     app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
#     db.init_app(app)
#
#     with app.app_context():
#         from . import webapp
#         db.create_all()
#
#         return app
